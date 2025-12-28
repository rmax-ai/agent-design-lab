# Questions & Feedback Needed - exp-001-role-vs-goal

## Pre-Execution Questions

### 1. Harness Components ✅ ANSWERED
- **Q**: Are harness components (agents, evaluators, workflows) already implemented?
- **Status**: Scaffolded but not implemented (README-only placeholders)
- **Impact**: Required for steps 6-12
- **Resolution**: Harness implementation needed before pilot runs can execute

### 2. Task Definition ✅ ANSWERED
- **Q**: Are there existing task templates or examples to follow?
- **Status**: Created comprehensive task suite with 6 tasks
- **Impact**: Step 2 complete

### 3. Statistical Analysis Tools
- **Q**: What tools/libraries should be used for statistical analysis in step 9?
- **Consideration**: Python (scipy, pandas), R, or other?
- **Impact**: Affects step 9 implementation
- **Recommendation**: Python with scipy.stats for paired t-tests, pandas for data manipulation

### 4. Evaluation Metrics ✅ ANSWERED
- **Q**: What specific metrics should be pre-registered?
- **Status**: 9 metrics defined in research.md
- **Impact**: Step 1 complete

### 5. Run Infrastructure ✅ PARTIALLY ANSWERED
- **Q**: How are runs actually executed? Manual, automated, or through specific harness workflows?
- **Status**: Workflow references exist (pin-and-run, replay, synthesize) but not implemented
- **Impact**: Critical for steps 6-7
- **Resolution**: Harness workflows need implementation

## Ongoing Questions

### 6. Pilot Run Execution (NEW - Step 6)
- **Q**: Without implemented harness workflows, how should pilot runs proceed?
- **Options**:
  a) Implement minimal harness workflows for pilot
  b) Simulate pilot runs with mock data to validate templates
  c) Document pilot plan and defer to implementation team
- **Status**: NEEDS CLARIFICATION
- **Impact**: Blocks steps 6-12

### 7. Harness Implementation Scope
- **Q**: Is harness implementation part of this execution plan task, or a separate effort?
- **Consideration**: Execution plan says "ensure harness/evaluators produce..." but doesn't specify building them
- **Status**: NEEDS CLARIFICATION
- **Impact**: Determines whether we proceed with implementation or planning only

### 8. Experiment Timeline
- **Q**: The execution plan estimates 1-3 days for prep, 1-4 days for runs. Is this a planning exercise or full implementation?
- **Status**: NEEDS CLARIFICATION
- **Impact**: Determines scope of remaining steps

