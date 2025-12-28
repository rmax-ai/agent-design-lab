# Next Steps - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Design Phase Complete → Transition to Implementation

---

## Executive Summary

The **design phase is complete** with 18 comprehensive documents and 13 functional scripts. The experiment is now ready to transition from planning to implementation and execution. This document outlines the critical path forward, prioritized actions, and decision points needed to move to pilot runs and full experiment execution.

**Current State**: All designs, specifications, and plans complete  
**Next Milestone**: Execute pilot runs (2 tasks × 2 variants = 4 runs)  
**Critical Blocker**: Implementation validation and environment setup  

---

## Immediate Next Steps (Week 1)

### Priority 1: Implementation Validation & Setup

#### 1.1 Verify Harness Scripts are Functional ⚡ HIGH PRIORITY

**Status**: Scripts created but not tested  
**Effort**: 2-4 hours  
**Owner**: Implementation team or pilot executor

**Actions**:
```bash
# Test evaluator modules
cd /path/to/agent-design-lab

# Create test data
mkdir -p /tmp/test-eval
echo '{"task_id": "TEST", "success_criteria": ["file_exists"]}' > /tmp/test-eval/task.json
echo '{"file_path": "/tmp/test-eval/output.txt"}' > /tmp/test-eval/expected.json
echo '{"violations": []}' > /tmp/test-eval/agent_outputs.json

# Test task_success evaluator
python3 harness/evaluators/task_success.py \
  --task-spec /tmp/test-eval/task.json \
  --agent-outputs /tmp/test-eval/agent_outputs.json \
  --expected-outputs /tmp/test-eval/expected.json \
  --output /tmp/test-eval/results.json

# Expected: Creates results.json with evaluation
cat /tmp/test-eval/results.json

# Repeat for other evaluators...
```

**Success Criteria**:
- ✅ All 5 evaluators run without errors
- ✅ Evaluators produce valid JSON output
- ✅ Workflow scripts accept arguments correctly
- ✅ lock-run.sh modifies manifests as expected

**Blockers to Resolve**:
- Missing dependencies (pandas, scipy, statsmodels) → Install via pip
- Path issues → Update scripts with correct relative paths
- Permission issues → Ensure scripts are executable (chmod +x)

**Output**: Test results document confirming all scripts operational

---

#### 1.2 Set Up Experiment Environment ⚡ HIGH PRIORITY

**Status**: Not started  
**Effort**: 1-2 hours  
**Owner**: Experiment executor

**Actions**:
```bash
# 1. Create experiment directory structure
cd experiments/exp-001-role-vs-goal
mkdir -p runs/pilot
mkdir -p data/inputs
mkdir -p data/outputs
mkdir -p logs

# 2. Install Python dependencies
pip install pandas scipy statsmodels matplotlib numpy

# 3. Verify task input files exist or create them
# (For TASK-002, TASK-005 which need pre-populated files)
cd tasks/TASK-002
# Create sample config files for testing

# 4. Set up logging
mkdir -p logs/pilot
touch logs/pilot/execution.log

# 5. Create .gitignore for runtime artifacts
cat >> .gitignore <<EOF
# Experiment runtime artifacts
experiments/*/runs/*/outputs/
experiments/*/runs/*/logs/
experiments/*/data/outputs/
*.pyc
__pycache__/
EOF
```

**Success Criteria**:
- ✅ Directory structure in place
- ✅ Python dependencies installed
- ✅ Task input files prepared
- ✅ Logging configured
- ✅ .gitignore prevents committing runtime data

**Output**: Environment ready for pilot runs

---

#### 1.3 Create Pilot Run Manifests 🔴 CRITICAL PATH

**Status**: Template exists, instances needed  
**Effort**: 1-2 hours  
**Owner**: Experiment executor

**Actions**:
```bash
# For each pilot run, create manifest from template

# Run 1: TASK-001 × role-centric
cp run-manifest-template.md runs/pilot/run-001-role-task001-manifest.json
# Edit manifest:
#   - run_id: "run-001-role-task001-2025-12-28"
#   - variant: "role-centric"
#   - task: "TASK-001"
#   - seed: 42
#   - timestamp: current

# Run 2: TASK-001 × goal-centric
# Similar process...

# Run 3: TASK-002 × role-centric
# Similar process...

# Run 4: TASK-002 × goal-centric
# Similar process...
```

**Alternative (Automated)**:
```python
# Create generate-pilot-manifests.py script
python3 scripts/generate-pilot-manifests.py \
  --tasks TASK-001,TASK-002 \
  --variants role-centric,goal-centric \
  --output runs/pilot/
```

**Success Criteria**:
- ✅ 4 manifest.json files created
- ✅ All pins populated (harness version, evaluator versions)
- ✅ All fields valid (no placeholders)
- ✅ Manifests pass validation script

**Validation**:
```bash
python3 harness/workflows/validate-manifest.py \
  --manifest runs/pilot/run-001-role-task001-manifest.json
# Expected: "✓ VALIDATION PASSED"
```

**Output**: 4 validated manifest files ready for execution

---

### Priority 2: Pilot Execution (First Run)

#### 2.1 Execute First Pilot Run (Smoke Test) 🔴 CRITICAL PATH

**Status**: Not started  
**Effort**: 1-2 hours (includes debugging)  
**Owner**: Experiment executor

**Run**: TASK-001 (Simple File Creation) × role-centric variant

**Actions**:
```bash
# 1. Load manifest
MANIFEST="runs/pilot/run-001-role-task001-manifest.json"

# 2. Set up run directory
RUN_ID=$(jq -r '.run_id' $MANIFEST)
RUN_DIR="runs/pilot/$RUN_ID"
mkdir -p $RUN_DIR

# 3. Execute task (manual simulation for pilot)
# In production: harness/workflows/pin-and-run.sh would do this
# For pilot: manually execute following role-centric spec

# Read variant specification
cat variants/role-centric.md

# Read task specification
cat tasks/TASK-001/spec.json

# Execute task per specification
# (This is where agent would run - for pilot, do manually or with mock agent)

# 4. Capture outputs
mkdir -p $RUN_DIR/outputs
# Copy any files created during task execution

# 5. Create execution log
cat > $RUN_DIR/agent.log <<EOF
{
  "run_id": "$RUN_ID",
  "start_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)",
  "end_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.%3NZ)",
  "events": [],
  "entries": []
}
EOF

# 6. Evaluate run
python3 harness/workflows/evaluate.py --manifest $MANIFEST

# 7. Lock run
bash harness/workflows/lock-run.sh $MANIFEST

# 8. Review scorecard
cat $RUN_DIR/scorecard.json
```

**Success Criteria**:
- ✅ Run completes without errors
- ✅ Scorecard generated with all metrics
- ✅ Manifest locked
- ✅ Outputs captured in run directory

**If Issues Arise**:
- Document all errors in `logs/pilot/issues.md`
- Update harness scripts as needed
- Rerun with fixes

**Output**: Completed first pilot run with scorecard

---

#### 2.2 Execute Remaining Pilot Runs

**Status**: Depends on 2.1 success  
**Effort**: 2-4 hours  
**Owner**: Experiment executor

**Actions**:
```bash
# Repeat 2.1 process for:
# - Run 2: TASK-001 × goal-centric
# - Run 3: TASK-002 × role-centric  
# - Run 4: TASK-002 × goal-centric

# After all runs complete, verify pairing
python3 harness/workflows/verify-pairing.py \
  --pair-id "pair-001-TASK-001" \
  --manifests runs/pilot/run-001-*/manifest.json runs/pilot/run-002-*/manifest.json
```

**Success Criteria**:
- ✅ 4 pilot runs complete
- ✅ 2 pairs verified
- ✅ All scorecards generated
- ✅ No critical issues

**Output**: Complete pilot run dataset

---

#### 2.3 Analyze Pilot Results

**Status**: Depends on 2.2 success  
**Effort**: 1-2 hours  
**Owner**: Experiment executor / analyst

**Actions**:
```bash
# 1. Create scorecard index
python3 scripts/create-scorecard-index.py \
  --run-dir runs/pilot \
  --output runs/pilot/scorecard-index.csv

# 2. Verify sample size (should be 2 pairs, not 10)
python3 analysis/verify_sample_size.py \
  --scorecard-index runs/pilot/scorecard-index.csv \
  --min-samples 1
# Note: Pilot has n=1 per task, not n=10

# 3. Compute aggregates
python3 analysis/compute_aggregates.py \
  --scorecard-index runs/pilot/scorecard-index.csv \
  --output runs/pilot/pilot-summary.csv

# 4. Visual inspection
cat runs/pilot/pilot-summary.csv

# 5. Document findings
cat > runs/pilot/PILOT-RESULTS.md <<EOF
# Pilot Results

## Summary
- Runs completed: 4/4
- Pairs verified: 2/2
- Issues encountered: [list]

## Metrics Overview
[paste summary from pilot-summary.csv]

## Workflow Validation
- Task execution: [pass/fail with notes]
- Evaluation: [pass/fail with notes]
- Pairing verification: [pass/fail with notes]

## Recommendations for Full Runs
1. [improvements identified]
2. [configuration changes needed]
3. [issues to address]
EOF
```

**Success Criteria**:
- ✅ Pilot results analyzed
- ✅ Workflow validated or issues documented
- ✅ Go/no-go decision for full runs

**Output**: PILOT-RESULTS.md with recommendations

---

## Short-term Next Steps (Week 2-3)

### Priority 3: Full Run Preparation

#### 3.1 Address Pilot Issues

**Status**: Depends on pilot results  
**Effort**: Variable (2-8 hours)  
**Owner**: Implementation team

**Actions**:
- Fix any bugs discovered in pilot
- Update harness scripts based on learnings
- Refine evaluation criteria if needed
- Document all changes

**Success Criteria**:
- ✅ All pilot issues resolved
- ✅ Updated scripts tested
- ✅ Changes documented

---

#### 3.2 Scale Up Infrastructure

**Status**: Post-pilot  
**Effort**: 4-8 hours  
**Owner**: Experiment executor

**Actions**:
```bash
# 1. Prepare full run directory structure
mkdir -p runs/full/{pair-001..pair-030}

# 2. Generate 180 manifests (6 tasks × 15 pairs × 2 variants)
python3 scripts/generate-full-manifests.py \
  --tasks TASK-001,TASK-002,TASK-003,TASK-004,TASK-005,TASK-006 \
  --variants role-centric,goal-centric \
  --pairs 15 \
  --output runs/full/

# 3. Validate all manifests
for manifest in runs/full/*/manifest.json; do
  python3 harness/workflows/validate-manifest.py --manifest $manifest
done

# 4. Create execution schedule
python3 scripts/create-execution-schedule.py \
  --manifests runs/full/*/manifest.json \
  --interleave \
  --output runs/full/EXECUTION-SCHEDULE.md

# 5. Set up batch execution (if automating)
# Or prepare manual execution checklist
```

**Success Criteria**:
- ✅ 180 manifests generated and validated
- ✅ Execution schedule created
- ✅ Infrastructure ready for full runs

---

#### 3.3 Execute Full Runs

**Status**: Post-pilot, infrastructure ready  
**Effort**: 2-5 days (depending on automation level)  
**Owner**: Experiment executor

**Approach A: Automated (Preferred)**
```bash
# Execute all runs via script
python3 scripts/execute-full-runs.py \
  --schedule runs/full/EXECUTION-SCHEDULE.md \
  --parallel 4 \
  --log runs/full/execution.log
```

**Approach B: Manual (Slower but more controlled)**
```bash
# Execute runs in batches following schedule
# Document progress in runs/full/PROGRESS.md
```

**During Execution**:
- Monitor for QA violations
- Check constraint adherence in real-time
- Document any anomalies
- Pause if critical issues arise

**Success Criteria**:
- ✅ All 180 runs complete
- ✅ All scorecards generated
- ✅ All pairs verified
- ✅ No systematic issues

---

### Priority 4: Analysis & Reporting

#### 4.1 Statistical Analysis

**Status**: After full runs complete  
**Effort**: 4-8 hours  
**Owner**: Data analyst / experiment executor

**Actions**:
```bash
# 1. Create scorecard index
python3 scripts/create-scorecard-index.py \
  --run-dir runs/full \
  --output runs/full/scorecard-index.csv

# 2. Verify sample size
python3 analysis/verify_sample_size.py \
  --scorecard-index runs/full/scorecard-index.csv \
  --min-samples 10

# 3. Test primary hypothesis (H1)
python3 analysis/test_h1_task_success.py \
  --scorecard-index runs/full/scorecard-index.csv \
  --output runs/full/h1-results.json

# 4. Test secondary hypotheses (H2-H5)
# Similar scripts for each hypothesis

# 5. Apply Bonferroni correction
python3 analysis/bonferroni_correction.py \
  --p-values [from H1-H5] \
  --hypothesis-names H1,H2,H3,H4,H5 \
  --output runs/full/corrected-results.json

# 6. Compute effect sizes
python3 analysis/effect_sizes.py \
  --scorecard-index runs/full/scorecard-index.csv \
  --output runs/full/effect-sizes.json

# 7. Generate visualizations
python3 analysis/plot_success_rates.py \
  --scorecard-index runs/full/scorecard-index.csv \
  --output report/figures/
```

**Success Criteria**:
- ✅ All statistical tests complete
- ✅ Effect sizes computed
- ✅ Visualizations generated
- ✅ Results statistically valid

---

#### 4.2 Write Comparative Report

**Status**: After analysis complete  
**Effort**: 8-16 hours  
**Owner**: Experiment lead / researcher

**Actions**:
```bash
# Use closure-plan.md as template
# Follow structure in closure-plan.md section 10

# Create report
cd report/
touch comparative-report.md

# Sections to complete:
# 1. Abstract (200 words)
# 2. Introduction (research question, motivation)
# 3. Methods (pre-registration, tasks, variants, metrics, procedure)
# 4. Results (descriptive stats, hypothesis tests, visualizations)
# 5. Discussion (interpretation, limitations, implications)
# 6. Conclusions (summary, recommendations)
# 7. References (pre-registration, specs, harness docs)
# 8. Appendices (raw data, statistical details, reproducibility info)
```

**Success Criteria**:
- ✅ Complete report written
- ✅ All claims supported by data
- ✅ Transparent about limitations
- ✅ Actionable recommendations

---

#### 4.3 Reproducibility Verification

**Status**: After report drafted  
**Effort**: 2-4 hours  
**Owner**: Independent reviewer or experiment executor

**Actions**:
```bash
# 1. Replay select runs to verify reproducibility
python3 harness/workflows/replay.py \
  --original-run runs/full/run-042-*/manifest.json \
  --replay-run runs/replay/run-042-replay/manifest.json

# 2. Compare outputs
python3 harness/evaluators/reproducibility.py \
  --runs runs/full/run-042-*/manifest.json runs/replay/run-042-replay/manifest.json \
  --output runs/replay/reproducibility-check.json

# 3. Document reproducibility score
# Add to report appendix

# 4. Archive all artifacts
tar -czf exp-001-role-vs-goal-archive.tar.gz \
  experiments/exp-001-role-vs-goal/
```

**Success Criteria**:
- ✅ Replay successful
- ✅ Reproducibility verified
- ✅ Archive created
- ✅ Report complete

---

## Decision Points

### Decision 1: Pilot Go/No-Go (After Priority 2)

**When**: After pilot results analyzed  
**Decision**: Proceed to full runs OR iterate on design

**Criteria for GO**:
- ✅ Pilot runs completed successfully
- ✅ Workflow validated
- ✅ Evaluation metrics sensible
- ✅ No critical blockers

**Criteria for NO-GO (iterate)**:
- ❌ Systematic evaluation failures
- ❌ Task specifications ambiguous
- ❌ Variant parity violated
- ❌ Technical infrastructure issues

**Fallback**: If NO-GO, address issues and rerun pilot

---

### Decision 2: Automation Level (Before Priority 3)

**When**: After pilot success, before full runs  
**Decision**: Automated execution OR manual execution

**Automated (Recommended if)**:
- Large run count (180 runs)
- Harness scripts stable
- Infrastructure robust

**Manual (Recommended if)**:
- Pilot revealed instability
- Need tight control
- Learning/debugging focus

---

### Decision 3: Early Stopping (During Priority 3)

**When**: During full runs, if issues detected  
**Decision**: Continue OR pause/stop

**Continue if**:
- Issues are minor/isolated
- Overall data quality good
- Sufficient pairs collected

**Pause/Stop if**:
- Systematic evaluation failures
- Data quality compromised
- Design flaw discovered

---

## Risk Mitigation

### Risk 1: Harness Scripts Have Bugs 🔴 HIGH

**Mitigation**:
- Test thoroughly in Priority 1
- Start with pilot (small n)
- Manual review of first results
- Gradual scale-up

**Contingency**: Fix bugs and rerun affected runs

---

### Risk 2: Task Definitions Ambiguous 🟡 MEDIUM

**Mitigation**:
- Pilot will reveal ambiguities
- Clarify before full runs
- Document all clarifications

**Contingency**: If discovered during full runs, add to limitations section

---

### Risk 3: Insufficient Statistical Power 🟡 MEDIUM

**Mitigation**:
- Pre-registered n=15 pairs per task (90 per variant)
- Power analysis in advance
- Can extend if needed

**Contingency**: Report null findings with power analysis, recommend follow-up

---

### Risk 4: Infrastructure Failures 🟡 MEDIUM

**Mitigation**:
- Checkpoint after each run
- Save manifests immediately
- Immutability ensures no data loss
- Can resume from any point

**Contingency**: Rerun failed runs, verify reproducibility

---

## Success Metrics

### Pilot Success
- ✅ 4 runs complete (2 tasks × 2 variants)
- ✅ 2 pairs verified
- ✅ Workflow validated
- ✅ No critical blockers

### Full Runs Success
- ✅ 180 runs complete (6 tasks × 15 pairs × 2 variants)
- ✅ 90 pairs verified
- ✅ <5% QA violations
- ✅ All evaluations successful

### Analysis Success
- ✅ All hypothesis tests complete
- ✅ Statistical assumptions met
- ✅ Effect sizes computed
- ✅ Visualizations generated

### Report Success
- ✅ Complete comparative report
- ✅ Peer-reviewable quality
- ✅ Reproducibility verified
- ✅ Actionable recommendations

---

## Resource Requirements

### Personnel
- **Experiment Executor**: 2-3 weeks full-time
- **Data Analyst**: 1 week full-time (analysis phase)
- **Independent Reviewer**: 4-8 hours (reproducibility check)

### Infrastructure
- **Compute**: Sufficient for 180 agent runs (depends on agent complexity)
- **Storage**: ~10GB for runs, logs, outputs
- **Software**: Python 3.8+, pandas, scipy, statsmodels, matplotlib

### Timeline
- **Week 1**: Validation, setup, pilot (Priority 1-2)
- **Week 2-3**: Full runs (Priority 3)
- **Week 4**: Analysis, reporting (Priority 4)
- **Total**: ~4 weeks from start to complete report

---

## Communication Plan

### Checkpoints
1. **After Priority 1**: Infrastructure validated
2. **After Priority 2**: Pilot complete, go/no-go decision
3. **After Priority 3**: Full runs complete
4. **After Priority 4**: Report ready for review

### Stakeholder Updates
- Weekly status emails
- Checkpoint presentations
- Final report presentation

---

## Appendix: Quick Reference Commands

### Setup
```bash
# Install dependencies
pip install pandas scipy statsmodels matplotlib numpy

# Create directories
mkdir -p experiments/exp-001-role-vs-goal/{runs/pilot,data/{inputs,outputs},logs}
```

### Pilot Execution
```bash
# Generate manifests
python3 scripts/generate-pilot-manifests.py --output runs/pilot/

# Validate manifest
python3 harness/workflows/validate-manifest.py --manifest runs/pilot/run-001-*/manifest.json

# Execute (manual or via harness)
# [task execution here]

# Evaluate
python3 harness/workflows/evaluate.py --manifest runs/pilot/run-001-*/manifest.json

# Lock
bash harness/workflows/lock-run.sh runs/pilot/run-001-*/manifest.json
```

### Analysis
```bash
# Create index
python3 scripts/create-scorecard-index.py --run-dir runs/full --output runs/full/scorecard-index.csv

# Test H1
python3 analysis/test_h1_task_success.py --scorecard-index runs/full/scorecard-index.csv --output runs/full/h1-results.json

# Visualize
python3 analysis/plot_success_rates.py --scorecard-index runs/full/scorecard-index.csv --output report/figures/
```

---

## Document Control

**Version**: 1.0  
**Author**: Experiment Design Agent  
**Date**: 2025-12-28  
**Last Updated**: 2025-12-28  
**Next Review**: After pilot completion  

**Change Log**:
- 2025-12-28: Initial version created

---

**Status**: READY FOR EXECUTION  
**Next Action**: Begin Priority 1 (Implementation Validation & Setup)  
**Estimated Start Date**: [To be determined]  
**Expected Completion**: [Start date + 4 weeks]
