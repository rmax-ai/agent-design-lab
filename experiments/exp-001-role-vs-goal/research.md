# Research Brief: exp-001-role-vs-goal

**Experiment ID**: exp-001-role-vs-goal  
**Status**: Pre-registration (locked before first pinned run)  
**Date**: 2025-12-28  
**Version**: 1.0

---

## 1. Objective

Compare **role-centric (anthropomorphic)** agent specifications against **goal-centric (first-principles)** agent specifications under controlled, identical conditions to determine which paradigm produces superior outcomes across task completion, constraint adherence, and reproducibility.

See project/manifest.md for experiment contract and structure.

---

## 2. PRE-REGISTERED HYPOTHESES

### Primary Hypothesis (H1)
**Goal-centric agent specifications will demonstrate higher task success rates than role-centric specifications when controlling for identical tooling, constraints, and evaluation criteria.**

**Rationale**: Role-centric specifications may introduce ambiguity through anthropomorphic metaphors, while goal-centric specifications provide explicit, measurable objectives that reduce interpretation variance.

### Secondary Hypotheses

**H2: Constraint Adherence**  
Goal-centric agents will show better adherence to explicit constraints due to clearer specification of boundaries and invariants.

**H3: Reproducibility**  
Goal-centric agents will demonstrate higher reproducibility (lower variance across runs with identical seeds) due to reduced ambiguity in specification.

**H4: Clarification Requests**  
Role-centric agents will require more clarification requests due to implicit assumptions and underspecified behavior boundaries.

**H5: Runtime Efficiency**  
No significant difference in runtime between paradigms when controlling for task complexity and tooling.

---

## 3. PRE-REGISTERED METRICS

### Primary Metrics

1. **Task Success Rate** (binary: pass/fail)
   - Definition: Task produces expected output within constraints
   - Measurement: Automated evaluator checks against expected outputs
   - Target: Per-task and aggregate success rates

2. **Constraint Adherence Score** (0-100 scale)
   - Definition: Percentage of constraints satisfied during execution
   - Measurement: Evaluator checks logs for constraint violations
   - Components:
     - Tool permission boundaries
     - File system scoping rules
     - Immutability requirements
     - Logging completeness

### Secondary Metrics

3. **Clarification Request Count** (integer)
   - Definition: Number of times agent requests user input/clarification
   - Measurement: Parse agent logs for clarification patterns
   - Expected: Lower is better (indicates clearer specification)

4. **Runtime (seconds)** (continuous)
   - Definition: Wall-clock time from task start to completion
   - Measurement: Harness timestamps
   - Control: Timeout at 600 seconds (10 minutes) per task

5. **Reproducibility Score** (0-1 scale)
   - Definition: Fraction of identical outputs across repeated runs with same seed
   - Measurement: Hash comparison of outputs and intermediate states
   - Target: ≥0.95 for acceptable reproducibility

6. **Specification Clarity** (qualitative → quantitative)
   - Definition: Subjective assessment converted to structured rubric
   - Measurement: Expert review on 5-point scale
   - Rubric: Explicitness, completeness, ambiguity level

### Tertiary Metrics (Exploratory)

7. **Log Volume** (lines/bytes)
8. **Tool Invocation Patterns** (frequency distribution)
9. **Error Recovery Attempts** (count)

---

## 4. STATISTICAL ANALYSIS PLAN

### Sample Size
- **Minimum**: 10 paired runs per task
- **Target**: 15 paired runs per task for robustness
- **Pairing**: Each run pair uses identical task inputs, seeds, and environmental conditions

### Statistical Tests

**Primary Analysis**: Paired t-test on task success rates
- Pairing: Same task, different specification paradigm
- Alpha: 0.05 (two-tailed)
- Effect size: Cohen's d
- Null hypothesis: No difference in mean success rates

**Secondary Analyses**:
1. **Constraint Adherence**: Wilcoxon signed-rank test (non-parametric alternative)
2. **Clarification Requests**: Paired t-test or Wilcoxon
3. **Runtime**: Paired t-test with log transformation if needed
4. **Reproducibility**: Paired t-test on reproducibility scores

**Correction for Multiple Comparisons**: Bonferroni correction for family-wise error rate

### Effect Size Thresholds
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

### Success Criteria
**Experiment succeeds if**:
- All ≥10 paired runs completed successfully
- Statistical power ≥0.80 for primary hypothesis
- Reproducibility ≥0.90 for at least 80% of runs
- Results statistically significant (p < 0.05) OR
- Results clearly non-significant with sufficient power (accept null)

**Practical Significance Threshold**:
- Minimum detectable difference: 15% improvement in primary metric
- Below this threshold, differences considered practically negligible

---

## 5. EXPERIMENTAL DESIGN

### Variables

**Independent Variable**: Agent specification paradigm (2 levels)
- Role-centric: Uses personas, roles, anthropomorphic language
- Goal-centric: Uses objectives, constraints, first-principles

**Controlled Variables** (identical across variants):
- Task suite (same tasks for both)
- Tool access permissions
- Constraint set
- Evaluation criteria
- Harness version (pinned per run)
- Evaluator versions (pinned per run)
- Random seeds (paired across variants)
- Environmental conditions

**Dependent Variables**: See metrics above

### Pairing Policy
- Each task executed by both variants with identical:
  - Input specification
  - Random seed
  - Timeout settings
  - Tool access
- Runs interleaved to minimize temporal bias
- Run order randomized within pairs

---

## 6. TASK SUITE REQUIREMENTS

Tasks must be:
1. **Deterministic**: Same inputs → same outputs (given seed)
2. **Representative**: Cover realistic agent operations
3. **Graded**: Range from simple to complex
4. **Evaluable**: Clear success criteria
5. **Constraint-bounded**: Exercise permission and scoping rules

**Minimum Task Types**:
- File manipulation (read, write, edit)
- Multi-step reasoning
- Tool composition
- Error handling
- Constraint navigation

---

## 7. DATA COLLECTION & STORAGE

### Run Artifacts (per run)
- Run manifest (JSON): pins, metadata, configuration
- Agent logs: complete execution trace
- Evaluator scorecard: structured metrics
- Output artifacts: task deliverables
- Timing data: timestamps for all phases

### Storage Structure
```
runs/
  run-{timestamp}-{variant}-{task}/
    manifest.json
    agent.log
    scorecard.json
    outputs/
    timing.json
```

### Immutability
- Completed runs are immutable
- Corrections require new runs with incremented version
- All scorecards append-only

---

## 8. QUALITY ASSURANCE

### Pre-Run Validation
- Manifest schema validation
- Pin verification (no floating versions)
- Task determinism smoke test
- Evaluator calibration

### Post-Run Validation
- Scorecard completeness check
- Log integrity verification
- Constraint violation audit
- Reproducibility spot-check

### Violation Handling
- All violations logged immediately
- Critical violations halt experiment
- Non-critical violations documented with rationale
- Remediation policy: re-run with fixes vs. document and continue

---

## 9. ANALYSIS PIPELINE

### Phase 1: Data Aggregation
- Collect all scorecards
- Validate completeness
- Compute aggregate statistics

### Phase 2: Statistical Testing
- Execute pre-registered tests
- Compute effect sizes and confidence intervals
- Check assumptions (normality, etc.)

### Phase 3: Visualization
- Success rate comparison (bar charts)
- Distribution plots for continuous metrics
- Scatter plots for paired comparisons
- Reproducibility heatmaps

### Phase 4: Interpretation
- Evidence-based conclusions
- Practical significance assessment
- Limitation documentation
- Follow-up recommendations

---

## 10. TERMINATION CONDITIONS

**Experiment completes when**:
- ✅ ≥10 paired runs per task completed
- ✅ All runs reproducible within tolerance (≥90%)
- ✅ Statistical analysis complete
- ✅ Comparative report generated
- ✅ Design recommendations derived from evidence

**Early Termination Triggers**:
- Insurmountable technical barriers
- Systematic reproducibility failures (<70%)
- Ethical concerns or safety issues

---

## 11. LIMITATIONS & RISKS

### Known Limitations
1. Task suite may not cover all real-world scenarios
2. Evaluation metrics may miss nuanced differences
3. Harness implementation may introduce unintended biases
4. Sample size constrained by computational resources

### Mitigation Strategies
1. Diverse task suite with expert review
2. Multiple complementary metrics
3. Paradigm-agnostic harness design
4. Power analysis to determine adequate sample size

### Risks
- **Reproducibility failures**: Harness instability or non-deterministic tasks
- **Specification ambiguity**: Variants not sufficiently different
- **Evaluator bias**: Metrics favor one paradigm unintentionally
- **Resource constraints**: Insufficient runs to detect effects

---

## 12. FOLLOW-UP EXPERIMENTS

Based on outcomes, potential follow-ups:
- **exp-002**: Hybrid specifications (role + goal)
- **exp-003**: Specification complexity vs. performance
- **exp-004**: Domain-specific variants (coding vs. research vs. operations)
- **exp-005**: Human-in-the-loop vs. autonomous specifications

---

## PRE-REGISTRATION LOCK

**This pre-registration is locked as of 2025-12-28.**

Any modifications to hypotheses, metrics, or analysis plan after this date must:
1. Be clearly marked as post-hoc
2. Include rationale for the change
3. Be distinguished from pre-registered analyses in the final report
4. Not replace pre-registered analyses (only supplement)

**Locked By**: Execution Agent  
**Lock Date**: 2025-12-28T19:22:00.000Z  
**Commit Hash**: [To be added after commit]

---

END OF PRE-REGISTRATION
