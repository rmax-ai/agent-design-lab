# Experiment Design Package Summary - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Design Phase COMPLETE - Ready for Implementation

---

## Overview

This document provides a comprehensive summary of the exp-001-role-vs-goal experiment design, including all planning artifacts created during the design phase (Steps 1-6) and execution plans for the implementation phase (Steps 7-12).

---

## Design Phase: COMPLETE ✅

### Core Design Artifacts

1. **research.md** - Pre-Registered Research Design
   - 5 hypotheses (1 primary, 4 secondary)
   - 9 metrics (primary, secondary, tertiary)
   - Statistical analysis plan (paired t-tests, n≥10, α=0.05, Bonferroni correction)
   - Quality assurance procedures
   - Termination conditions
   - Locked before first run

2. **tasks/task-suite.md** - Task Suite Specification
   - 6 deterministic tasks covering required categories
   - TASK-001: Simple File Creation (low complexity)
   - TASK-002: Multi-File Read and Summarize (medium complexity)
   - TASK-003: Constrained File Edit (constraint navigation)
   - TASK-004: Error Recovery (error handling)
   - TASK-005: Tool Composition (high complexity)
   - TASK-006: Specification Ambiguity Test (clarification behavior)
   - Fixed seeds (42-47), timeouts, expected outputs

3. **variants/role-centric.md** - Anthropomorphic Specification
   - Persona-based: "Helpful Task Execution Assistant"
   - Narrative instructions, working styles, communication guidelines
   - Human-relatable framing

4. **variants/goal-centric.md** - First-Principles Specification
   - Objective-based: "Goal-driven control system"
   - Formal objectives, constraints, control loops
   - Algorithmic specification

5. **variants/parity-check.md** - Parity Verification
   - Confirms only paradigm differs
   - Identical tooling, constraints, permissions, evaluation
   - Verification matrix and parity check script

6. **evaluator-config.md** - Evaluation Infrastructure
   - 5 evaluator modules:
     - Task Success (binary, criteria-based)
     - Constraint Adherence (0-100 score)
     - Runtime (seconds, phases)
     - Clarification Counter (pattern-based)
     - Reproducibility (0-1 score, hash comparison)
   - Scoring rubrics and algorithms
   - Scorecard JSON schema

7. **run-manifest-template.md** - Run Specification
   - Complete JSON schema for run manifests
   - Pinning strategy (harness, evaluators, tools, variants, tasks)
   - Pre-run validation script
   - Immutability contract (before/during/after execution)
   - Pairing strategy with interleaving

8. **pilot-plan.md** - Pilot Execution Plan
   - 2 tasks (TASK-001, TASK-002)
   - 2 paired runs = 4 total runs
   - 5-phase workflow: setup, execute pair 1, execute pair 2, validate, report
   - Success criteria, issue tracking templates
   - Pilot artifacts specification

### Supporting Documents

9. **status.md** - Progress Tracking
   - Current step status
   - Completed steps checklist
   - Next actions

10. **notes.md** - Execution Notes
    - Detailed observations and learnings
    - Discovery of harness implementation blocker
    - Exit criteria tracking per step

11. **suggestions.md** - Improvement Recommendations
    - Automation opportunities
    - Documentation improvements
    - Workflow clarity suggestions
    - Template reusability
    - Pre-registration rigor

12. **need-feedback.md** - Questions Requiring Clarification
    - Harness implementation scope
    - Pilot run execution approach
    - Experiment timeline expectations

---

## Implementation Phase: Plans Ready ⏸️

### Execution Plans

13. **full-runs-plan.md** - Full Experiment Execution
    - 6 tasks × 15 pairs × 2 variants = 180 runs
    - Temporal and task interleaving strategy
    - Quality assurance during execution (Step 8)
    - Violation handling (critical vs non-critical)
    - Progress tracking (registry.csv, violations.log)
    - Automation script templates

14. **analysis-plan.md** - Data Analysis Workflow
    - Data aggregation from scorecards
    - Pre-registered statistical tests (Steps 9)
    - Effect size estimation (Cohen's d)
    - Power analysis
    - Visualization generation (4 figure types)
    - Quality checks (normality, outliers, sensitivity)

15. **closure-plan.md** - Experiment Completion
    - Comparative report structure (Step 10)
    - Replay & reproducibility checks (Step 11)
    - Experiment closure & archiving (Step 12)
    - Lessons learned documentation
    - Follow-up experiment proposals

---

## Readiness Assessment

### Ready for Implementation ✅

**Specifications Complete**:
- ✅ Research design pre-registered and locked
- ✅ Task suite defined and frozen
- ✅ Agent variants specified with parity verification
- ✅ Evaluation instrumentation designed
- ✅ Run manifest schema defined
- ✅ Quality assurance procedures specified

**Plans Complete**:
- ✅ Pilot execution plan (Step 6)
- ✅ Full runs execution plan (Step 7)
- ✅ QA & violation handling plan (Step 8)
- ✅ Analysis plan (Step 9)
- ✅ Reporting plan (Step 10)
- ✅ Reproducibility plan (Step 11)
- ✅ Closure plan (Step 12)

**Documentation Complete**:
- ✅ Comprehensive notes and tracking
- ✅ Suggestions for improvement
- ✅ Questions identified for clarification

### Implementation Blocker 🚧

**Harness Components Not Implemented**:
- ❌ `harness/workflows/` - pin-and-run, replay, synthesize, evaluate, validate-manifest, lock-run
- ❌ `harness/evaluators/` - 5 evaluator module implementations
- ❌ `harness/agents/` - executor implementation
- ❌ `harness/schemas/` - JSON schemas for validation

**Impact**: Steps 6-12 cannot execute without functional harness

**Options**:
1. **Implement Harness** (separate effort, out of current scope)
2. **Defer to Implementation Team** (current recommendation)
3. **Mock Pilot** (simulate with mock data for template validation)

---

## Design Completeness Checklist

### Execution Plan Requirements

From execution-plan.md, design phase requirements:

**Step 1: Pre-register hypotheses** ✅
- [x] Explicit hypotheses defined
- [x] Primary/secondary metrics specified
- [x] Statistical tests planned
- [x] Minimum sample size (≥10 paired runs)
- [x] Success thresholds defined
- [x] Pre-registration locked before runs

**Step 2: Define & freeze task suite** ✅
- [x] Deterministic task specs created
- [x] Task IDs, inputs, seeds, timeouts, expected outputs
- [x] Sample inputs specified
- [x] Deterministic seed policies
- [x] Task suite frozen

**Step 3: Implement variant specs** ✅
- [x] Two variant descriptors created
- [x] Reference harness components
- [x] Parity check confirms identical tooling
- [x] Parity check confirms identical constraints
- [x] Parity check confirms identical permissions
- [x] Only specification paradigm differs

**Step 4: Instrument evaluation** ✅
- [x] Evaluators produce all pre-registered metrics
- [x] Evaluator versions pinnable
- [x] Evaluator config documented
- [x] Scoring rubrics defined
- [⏳] Evaluators produce deterministic scorecards (to validate in pilot)

**Step 5: Run manifest & pinning** ✅
- [x] Run manifest template created
- [x] Pinning policy specified
- [x] Pre-run validator defined
- [⏳] Manifest passes schema validation (to test in pilot)
- [⏳] Pre-run checks implemented (requires harness)

**Step 6: Pilot paired runs** ✅ (Planning)
- [x] Pilot plan created
- [x] 1-2 paired runs specified
- [x] Pilot artifacts defined
- [x] Issue log template provided
- [⏳] Pilot execution (blocked by harness)
- [⏳] Workflow validation (blocked by harness)

---

## Estimated Effort

From execution-plan.md estimates:

**Design & Prep (Steps 1-5)**: 1-3 days
- **Actual**: ~4 hours (design phase complete)
- **Status**: ✅ COMPLETE

**Pilot (Step 6)**: Part of prep
- **Estimated**: 0.5-1 day
- **Status**: ⏸️ Plan complete, execution blocked

**Full Runs + Validation (Steps 7-8)**: 1-4 days
- **Estimated**: Depends on per-run latency
- **Status**: ⏸️ Plan complete, execution blocked

**Analysis & Report (Steps 9-12)**: 1-3 days
- **Estimated**: 1-3 days
- **Status**: ⏸️ Plans complete, execution blocked

**Total Estimated**: 3-11 days (design through completion)
**Design Phase Actual**: ~4 hours

---

## Recommendations

### Immediate Next Steps

1. **Review Design Package**: Stakeholder review of all design artifacts
2. **Approve Pre-Registration**: Lock research.md as authoritative
3. **Prioritize Harness Implementation**: Separate initiative to build infrastructure
4. **Implement Minimal Harness**: Focus on pilot-required components first

### Implementation Strategy

**Phase A: Minimal Viable Harness** (for pilot)
- `pin-and-run` workflow (init + execute)
- Basic task success evaluator
- Basic constraint adherence checker
- Simple manifest validator
- Manual lock workflow

**Phase B: Full Harness** (for full runs)
- All 5 evaluator modules
- Automated workflows
- Replay capability
- Synthesize/aggregate capability

**Phase C: Execution** (Steps 6-12)
- Pilot runs
- Full runs
- Analysis
- Reporting
- Closure

### Success Criteria

**Design Phase**: ✅ COMPLETE
- All specifications documented
- All plans created
- Ready for implementation handoff

**Implementation Phase**: Ready to begin when harness available

---

## Appendix: File Manifest

### Created During Design Phase

```
experiments/exp-001-role-vs-goal/
├── research.md                    # Pre-registration (locked)
├── execution-plan.md              # Original 12-step plan
│
├── tasks/
│   ├── README.md                  # Task directory description
│   ├── task-suite.md              # Complete task suite specification
│   ├── TASK-001/
│   │   ├── spec.json              # Machine-readable task spec
│   │   └── README.md              # Human-readable description
│   ├── TASK-002/
│   │   └── spec.json
│   └── TASK-003/
│       └── spec.json
│
├── variants/
│   ├── README.md                  # Variants directory description
│   ├── role-centric.md            # Anthropomorphic specification
│   ├── goal-centric.md            # First-principles specification
│   └── parity-check.md            # Parity verification
│
├── evaluator-config.md            # Evaluator configurations & rubrics
├── run-manifest-template.md       # Run manifest schema & pinning
├── pilot-plan.md                  # Pilot execution plan (Step 6)
├── full-runs-plan.md              # Full runs plan (Step 7-8)
├── analysis-plan.md               # Analysis workflow (Step 9)
├── closure-plan.md                # Reporting & closure (Steps 10-12)
│
├── status.md                      # Progress tracking
├── notes.md                       # Execution notes
├── suggestions.md                 # Improvement recommendations
├── need-feedback.md               # Questions for clarification
└── SUMMARY.md                     # This document
```

**Total**: 16 markdown documents, 3 JSON specs, comprehensive design package

---

## Contact & Questions

For questions about this design package, refer to `need-feedback.md`.

For implementation planning, contact experiment lead or harness development team.

---

**Design Package Version**: 1.0  
**Completed**: 2025-12-28  
**Status**: Ready for Implementation Phase
