# Experiment Closure Plan - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Design complete, execution pending

---

## Overview

This document outlines the remaining steps (10-12) for completing the exp-001-role-vs-goal experiment.

---

## Step 10: Produce Comparative Report

### Report Structure

**experiments/exp-001-role-vs-goal/report/comparative-report.md**

```markdown
# Comparative Report: Role-Centric vs Goal-Centric Agent Specifications

**Experiment**: exp-001-role-vs-goal
**Date**: {completion_date}
**Status**: Complete

## Executive Summary
- Research question
- Key findings
- Recommendations
- Limitations

## 1. Introduction
- Background and motivation
- Research objectives
- Hypotheses

## 2. Methods
### 2.1 Experimental Design
- Paradigm definitions (role-centric vs goal-centric)
- Task suite description
- Pairing strategy

### 2.2 Materials
- Agent variant specifications
- Task specifications
- Harness version and configuration

### 2.3 Procedure
- Pre-registration process
- Pilot run summary
- Full run execution
- Quality assurance

### 2.4 Evaluation
- Evaluator descriptions
- Metrics and scoring
- Statistical methods

## 3. Results
### 3.1 Sample Characteristics
- Total runs: N
- Excluded runs: N (with reasons)
- Final sample: N paired runs per task

### 3.2 Primary Outcome (H1: Task Success)
- Descriptive statistics
- Statistical test results
- Effect size
- Confidence intervals
- Interpretation

### 3.3 Secondary Outcomes (H2-H5)
- Constraint adherence
- Reproducibility
- Clarification requests
- Runtime

### 3.4 Visualizations
- Figure 1: Success rate comparison
- Figure 2: Paired scatter plots
- Figure 3: Distribution plots
- Figure 4: Reproducibility heatmap

## 4. Discussion
### 4.1 Interpretation
- Support for hypotheses
- Practical significance
- Mechanism analysis

### 4.2 Comparison to Prior Work
- Related research
- Consistency with expectations

### 4.3 Limitations
- Sample size
- Task coverage
- Generalizability
- Measurement issues

### 4.4 Implications
- Design recommendations
- When to use role-centric specs
- When to use goal-centric specs
- Hybrid approaches

## 5. Conclusions
- Summary of evidence
- Recommendations for practitioners
- Future research directions

## 6. References
- Pre-registration document
- Task suite specifications
- Harness documentation
- Raw data and analysis code

## Appendices
### Appendix A: Raw Data Summary
- Link to runs/ directory
- Data dictionary
- Exclusion log

### Appendix B: Statistical Details
- Full test outputs
- Assumption checks
- Sensitivity analyses

### Appendix C: Reproducibility Information
- Harness version pins
- Evaluator version pins
- Analysis code repository
```

### Report Requirements

- **Evidence-based**: All claims supported by data
- **Transparent**: Methods fully described
- **Reproducible**: Links to all artifacts
- **Balanced**: Present limitations alongside findings
- **Actionable**: Clear recommendations

### Deliverables

1. `report/comparative-report.md` - Main report
2. `report/figures/` - All visualizations
3. `report/tables/` - Summary tables
4. `report/appendices/` - Supplementary materials

---

## Step 11: Replay & Reproducibility Checks

### Replay Selected Runs

**Purpose**: Verify run reproducibility using replay workflow

**Selection Criteria**:
- 1 run per task (6 total)
- Mix of variants (3 role-centric, 3 goal-centric)
- Include successful and failed runs
- Prioritize runs with interesting characteristics

**Replay Workflow**:

```bash
# For each selected run
./harness/workflows/replay \
  --manifest runs/run-{original-id}/manifest.json \
  --output runs/replay-{original-id}/

# Compare outputs
./harness/workflows/compare-runs \
  --original runs/run-{original-id}/ \
  --replay runs/replay-{original-id}/ \
  --tolerance-file replay-tolerances.json
```

**Comparison Checks**:
- Output files: Hash comparison (must match exactly)
- Scorecards: Metric comparison (within tolerance)
- Logs: Behavior comparison (major events must match)
- Runtime: Within ±20% variance acceptable

**Tolerance Specification** (`replay-tolerances.json`):
```json
{
  "output_hashes": "exact",
  "task_success": "exact",
  "constraint_adherence": "exact",
  "runtime": {"type": "relative", "tolerance": 0.20},
  "clarification_count": "exact",
  "reproducibility": {"type": "absolute", "tolerance": 0.05}
}
```

### Discrepancy Analysis

If replayed run differs from original:

1. **Document Difference**:
   - What changed?
   - Where in execution?
   - Magnitude of change?

2. **Classify Discrepancy**:
   - **Acceptable**: Within declared tolerance (e.g., timing variance)
   - **Explainable**: Due to known non-determinism (document source)
   - **Anomalous**: Unexpected difference (investigate)

3. **Impact Assessment**:
   - Does this affect conclusions?
   - Does this indicate systemic issue?
   - Should original run be flagged?

### Deliverables

1. `runs/replay-results.csv` - Comparison summary
2. `runs/discrepancy-analysis.md` - Detailed analysis
3. `report/reproducibility-appendix.md` - Reproducibility report

---

## Step 12: Close Experiment & Archive Outputs

### Termination Condition Verification

Check all conditions from project/manifest.md:

- ✅ ≥10 paired runs per task completed
- ✅ All runs reproducible within tolerance (≥90%)
- ✅ Comparative report generated
- ✅ Design recommendations derived from evidence

### Archive Preparation

**1. Organize Final Artifacts**

```
experiments/exp-001-role-vs-goal/
  research.md              # Pre-registration
  
  tasks/
    task-suite.md
    TASK-001/ ... TASK-006/
  
  variants/
    role-centric.md
    goal-centric.md
    parity-check.md
  
  runs/
    registry.csv
    progress.csv
    violations.log
    run-*/              # 180+ run directories
    replay-results.csv
  
  analysis/
    scorecard-index.csv
    variant-summary.csv
    statistical-tests.json
    effect-sizes.json
    analysis-notebook.ipynb
  
  report/
    comparative-report.md
    figures/
    tables/
    appendices/
  
  status.md
  notes.md
  suggestions.md
  need-feedback.md
```

**2. Copy to results/** (if experiment successful):

```bash
cp -r experiments/exp-001-role-vs-goal/ results/exp-001-role-vs-goal-complete/
```

**3. Generate Experiment Summary**

`experiments/exp-001-role-vs-goal/CLOSURE.md`:
```markdown
# Experiment Closure - exp-001-role-vs-goal

**Status**: COMPLETE
**Closed**: {date}
**Duration**: {start_date} to {end_date}

## Completion Checklist
- [x] ≥10 paired runs per task
- [x] All runs validated and immutable
- [x] Statistical analysis complete
- [x] Comparative report generated
- [x] Reproducibility verified
- [x] Recommendations documented

## Key Findings
- {Brief summary}

## Recommendations
- {Evidence-based recommendations}

## Follow-Up Experiments
- exp-002: {Proposed follow-up}

## Archive Location
- results/exp-001-role-vs-goal-complete/

## Final Statistics
- Total runs: N
- Total runtime: X hours
- Data volume: X MB
- Reproducibility rate: X%
```

### Lessons Learned

**Document in `experiments/exp-001-role-vs-goal/lessons-learned.md`**:
- What went well?
- What challenges were encountered?
- What would we do differently?
- What improvements to harness/process?

### Propose Follow-Ups

Based on findings, suggest:
- **exp-002**: Hybrid specifications (role + goal)
- **exp-003**: Specification complexity analysis
- **exp-004**: Domain-specific variants
- **exp-005**: Human-in-the-loop specifications

### Final Deliverables

1. `CLOSURE.md` - Experiment closure summary
2. `lessons-learned.md` - Retrospective
3. `follow-ups.md` - Proposed next experiments
4. Archive in `results/` - Complete experiment package
5. Updated project tracking - Mark experiment complete

---

## Exit Criteria (Project Termination Condition)

From project/manifest.md:

- ✅ Initial experiment has ≥10 paired runs
- ✅ All runs reproducible within declared tolerances
- ✅ Comparative report generated
- ✅ Design recommendations derived from evidence, not narrative

**PROJECT COMPLETE**: All termination conditions satisfied

---

**Status**: Plan ready, execution pending prior steps  
**Version**: 1.0  
**Created**: 2025-12-28T19:34:00.000Z
