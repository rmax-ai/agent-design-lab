# Pilot Run Plan - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Ready for execution (pending harness implementation)

---

## Purpose

Execute 1-2 paired runs over a small task subset to:
1. Validate experiment instrumentation and workflow
2. Test pin-and-run → execute → evaluate pipeline
3. Identify issues before full experiment
4. Validate manifest and scorecard schemas
5. Confirm evaluator outputs are acceptable

---

## Pilot Scope

### Task Selection

**Pilot Tasks** (2 tasks from suite):
1. **TASK-001**: Simple File Creation (low complexity, quick validation)
2. **TASK-002**: Multi-File Read and Summarize (medium complexity, tests multi-step reasoning)

**Rationale**:
- TASK-001: Basic functionality check, fast execution (~10-30 sec)
- TASK-002: More complex, tests file handling and JSON generation
- Combined: Covers file manipulation + multi-step reasoning
- Excludes high-complexity tasks for pilot (save for full runs)

### Paired Runs

**Pair 1**: TASK-001
- Run 1A: role-centric variant, TASK-001, seed=42
- Run 1B: goal-centric variant, TASK-001, seed=42

**Pair 2**: TASK-002
- Run 2A: goal-centric variant, TASK-002, seed=43 (reversed order)
- Run 2B: role-centric variant, TASK-002, seed=43

**Total**: 4 runs (2 pairs)

---

## Pilot Workflow

### Phase 1: Pre-Pilot Setup

**1.1 Implement Minimal Harness Components**

Required implementations:
```
harness/
  workflows/
    pin-and-run.sh          # Run orchestrator
    validate-manifest.py    # Manifest validator
    evaluate.py             # Evaluation dispatcher
    lock-run.sh             # Immutability locker
  
  evaluators/
    task_success.py         # Basic task success check
    constraint_adherence.py # Basic constraint check
    runtime.py              # Simple timing
    clarification_counter.py # Log pattern matching
    
  agents/
    executor.py             # Basic agent executor
```

**1.2 Prepare Test Inputs**

Create input files for pilot tasks:
```
experiments/exp-001-role-vs-goal/tasks/
  TASK-001/inputs/
    (none needed, creates fresh file)
  
  TASK-002/inputs/
    configs/
      app.yaml       (100 lines, predefined)
      database.yaml  (50 lines, predefined)
      logging.yaml   (30 lines, predefined)
```

**1.3 Setup Run Directory Structure**

```bash
mkdir -p experiments/exp-001-role-vs-goal/runs/pilot/
```

### Phase 2: Execute Pilot Pair 1 (TASK-001)

**2.1 Initialize Run 1A (role-centric, TASK-001)**

```bash
$ ./harness/workflows/pin-and-run --init \
    --experiment exp-001-role-vs-goal \
    --variant role-centric \
    --task TASK-001 \
    --seed 42 \
    --output experiments/exp-001-role-vs-goal/runs/pilot/run-001a/
```

Expected outputs:
- `manifest.json` with all pins
- Input snapshot (if any)
- Validation pass

**2.2 Validate Run 1A Manifest**

```bash
$ ./harness/workflows/validate-manifest.py \
    experiments/exp-001-role-vs-goal/runs/pilot/run-001a/manifest.json
```

Expected: VALIDATION PASSED

**2.3 Execute Run 1A**

```bash
$ ./harness/workflows/pin-and-run --execute \
    --manifest experiments/exp-001-role-vs-goal/runs/pilot/run-001a/manifest.json
```

Expected outputs:
- `agent.log` with execution trace
- `outputs/output.txt` (task deliverable)
- Updated manifest with execution metadata

**2.4 Evaluate Run 1A**

```bash
$ ./harness/workflows/evaluate.py \
    --manifest experiments/exp-001-role-vs-goal/runs/pilot/run-001a/manifest.json
```

Expected outputs:
- `scorecard.json` with all metrics
- `evaluation.log`

**2.5 Lock Run 1A**

```bash
$ ./harness/workflows/lock-run.sh \
    experiments/exp-001-role-vs-goal/runs/pilot/run-001a/manifest.json
```

Expected: `manifest.json` updated with `immutability.locked = true`

**2.6 Repeat 2.1-2.5 for Run 1B (goal-centric, TASK-001)**

Same workflow, different variant.

### Phase 3: Execute Pilot Pair 2 (TASK-002)

Repeat Phase 2 workflow for:
- Run 2A: goal-centric, TASK-002
- Run 2B: role-centric, TASK-002

### Phase 4: Pilot Validation

**4.1 Manifest Validation**

Check all 4 manifests:
- ✓ Schema compliance
- ✓ All pins present
- ✓ No floating versions
- ✓ Hashes correct
- ✓ Immutability locked

**4.2 Scorecard Validation**

Check all 4 scorecards:
- ✓ All metrics present
- ✓ Values within expected ranges
- ✓ Rationales provided
- ✓ Evaluator versions match manifest

**4.3 Pairing Validation**

Verify paired runs have:
- ✓ Identical task_id
- ✓ Identical seed
- ✓ Identical timeout
- ✓ Identical input snapshots (hash comparison)
- ✓ Different variant only

**4.4 Reproducibility Check**

Optional: Re-run one task with same seed:
- Run 1A-repeat: role-centric, TASK-001, seed=42
- Compare outputs to original Run 1A
- Verify hash match or document differences

---

## Pilot Success Criteria

### Must Pass (Critical)

1. ✓ All 4 runs complete without crashes
2. ✓ All manifests validate
3. ✓ All scorecards generated
4. ✓ Pins are correct and immutable
5. ✓ Evaluators execute deterministically

### Should Pass (Important)

6. ✓ Task success evaluator produces reasonable results
7. ✓ Constraint adherence tracks violations correctly
8. ✓ Runtime measurements accurate
9. ✓ Clarification counter finds patterns
10. ✓ Paired runs have identical inputs

### Nice to Have (Validation)

11. ~ Reproducibility check shows high score (≥0.90)
12. ~ Workflow runs smoothly without manual intervention
13. ~ Log quality sufficient for debugging

---

## Pilot Issue Tracking

### Issue Log Template

```markdown
### Issue {N}: {Brief Description}

**Severity**: Critical | Important | Minor  
**Component**: Harness | Evaluator | Manifest | Task | Variant  
**Observed**: {What went wrong}  
**Expected**: {What should have happened}  
**Impact**: {How this affects experiment}  
**Resolution**: {How to fix}  
**Status**: Open | Fixed | Deferred  
```

### Example Issues to Watch For

- **Issue 1**: Manifest validation fails due to schema mismatch
  - Severity: Critical
  - Resolution: Update schema or manifest template

- **Issue 2**: Evaluator produces non-deterministic scores
  - Severity: Critical
  - Resolution: Fix evaluator logic, ensure determinism

- **Issue 3**: Clarification counter misses patterns
  - Severity: Important
  - Resolution: Improve regex patterns

- **Issue 4**: Workflow requires manual steps
  - Severity: Minor
  - Resolution: Automate or document workaround

---

## Pilot Artifacts

After pilot completion, should have:

```
experiments/exp-001-role-vs-goal/runs/pilot/
  run-001a-role-centric-TASK-001/
    manifest.json
    agent.log
    outputs/
      output.txt
    scorecard.json
    evaluation.log
  
  run-001b-goal-centric-TASK-001/
    (same structure)
  
  run-002a-goal-centric-TASK-002/
    (same structure)
  
  run-002b-role-centric-TASK-002/
    (same structure)
  
  pilot-report.md              # Summary of pilot findings
  pilot-issues.md              # Issue log
  pilot-validation-results.md  # Validation checklist results
```

---

## Pilot Report Template

```markdown
# Pilot Run Report - exp-001-role-vs-goal

**Date**: {date}  
**Runs Completed**: {N}/4  
**Status**: Pass | Partial Pass | Fail  

## Summary
{Brief overview of pilot execution}

## Runs Executed
| Run ID | Variant | Task | Success | Runtime | Issues |
|--------|---------|------|---------|---------|--------|
| run-001a | role-centric | TASK-001 | ✓ | 15s | None |
| ... | ... | ... | ... | ... | ... |

## Validation Results
- Manifest validation: {Pass/Fail}
- Scorecard validation: {Pass/Fail}
- Pairing validation: {Pass/Fail}
- Reproducibility check: {Pass/Fail/Skipped}

## Issues Encountered
{List of issues with severity and status}

## Recommendations
{Changes needed before full runs}

## Go/No-Go Decision
{Ready for full runs? If no, what needs fixing?}
```

---

## Exit Criteria (from execution-plan.md)

From Step 6:
- ✓ 1-2 paired runs executed
- ✓ Run artifacts generated
- ✓ Issue log created
- ✓ No critical gaps identified
- ✓ Evaluator outputs acceptable
- ✓ Workflows validated

**Next Step**: If pilot passes, proceed to Step 7 (full runs). If issues, remediate and re-pilot.

---

**Status**: Ready for execution pending harness implementation  
**Version**: 1.0  
**Created**: 2025-12-28T19:30:00.000Z
