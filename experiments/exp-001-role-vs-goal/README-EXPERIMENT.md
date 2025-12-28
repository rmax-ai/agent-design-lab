# exp-001-role-vs-goal

**Experiment**: Comparing Role-Centric vs Goal-Centric Agent Specifications  
**Status**: Design Complete, Ready for Implementation  
**Date**: 2025-12-28

---

## Quick Start

### For Reviewers
Start with: **[SUMMARY.md](SUMMARY.md)** - Complete overview of the experiment design package

### For Implementers
1. Read: **[research.md](research.md)** - Pre-registered research design (locked)
2. Review: **[pilot-plan.md](pilot-plan.md)** - First execution target
3. Check: **[need-feedback.md](need-feedback.md)** - Open questions

### For Executors
1. Execute: **[pilot-plan.md](pilot-plan.md)** - Pilot runs (Steps 6)
2. Follow: **[full-runs-plan.md](full-runs-plan.md)** - Full experiment (Steps 7-8)
3. Analyze: **[analysis-plan.md](analysis-plan.md)** - Data analysis (Step 9)
4. Report: **[closure-plan.md](closure-plan.md)** - Reporting and closure (Steps 10-12)

---

## Document Guide

### Core Specifications

| Document | Purpose | Status |
|----------|---------|--------|
| [execution-plan.md](execution-plan.md) | Original 12-step execution plan | Reference |
| [research.md](research.md) | Pre-registered hypotheses, metrics, analysis | 🔒 LOCKED |
| [tasks/task-suite.md](tasks/task-suite.md) | 6 deterministic tasks | 🔒 FROZEN |
| [variants/role-centric.md](variants/role-centric.md) | Anthropomorphic specification | 🔒 FROZEN |
| [variants/goal-centric.md](variants/goal-centric.md) | First-principles specification | 🔒 FROZEN |
| [variants/parity-check.md](variants/parity-check.md) | Variant verification | ✅ VERIFIED |
| [evaluator-config.md](evaluator-config.md) | 5 evaluators & scoring rubrics | 🔒 FROZEN |
| [run-manifest-template.md](run-manifest-template.md) | Run schema & pinning strategy | ✅ COMPLETE |

### Execution Plans

| Document | Covers | Prerequisites | Status |
|----------|--------|---------------|--------|
| [pilot-plan.md](pilot-plan.md) | Step 6: Pilot runs | Harness implementation | 📋 READY |
| [full-runs-plan.md](full-runs-plan.md) | Steps 7-8: Full runs & QA | Successful pilot | 📋 READY |
| [analysis-plan.md](analysis-plan.md) | Step 9: Statistical analysis | Completed runs | 📋 READY |
| [closure-plan.md](closure-plan.md) | Steps 10-12: Report, replay, close | Analysis complete | 📋 READY |

### Progress Tracking

| Document | Purpose | Updated |
|----------|---------|---------|
| [status.md](status.md) | Progress checklist | Real-time |
| [notes.md](notes.md) | Detailed execution notes | Real-time |
| [suggestions.md](suggestions.md) | Improvement recommendations | As needed |
| [need-feedback.md](need-feedback.md) | Questions for clarification | As needed |
| [SUMMARY.md](SUMMARY.md) | Complete package overview | At milestones |

---

## Experiment Overview

### Research Question
Do goal-centric (first-principles) agent specifications produce better outcomes than role-centric (anthropomorphic) specifications?

### Hypothesis
Goal-centric specs → higher task success, better constraint adherence, higher reproducibility

### Method
- **Design**: Paired comparison (within-subjects)
- **Sample**: ≥10 paired runs per task (6 tasks)
- **Variants**: Role-centric vs Goal-centric (paradigm only differs)
- **Metrics**: Task success, constraint adherence, runtime, clarifications, reproducibility
- **Analysis**: Paired t-tests, effect sizes, confidence intervals

### Current Status
✅ **Design Phase**: Complete (Steps 1-6 + plans for 7-12)  
🚧 **Implementation Phase**: Blocked (requires harness)  
⏸️ **Execution Phase**: Pending

---

## Key Findings (So Far)

### Design Phase Learnings

1. **Pre-Registration Works**: Locking hypotheses before data collection ensures integrity
2. **Parity Critical**: Must verify variants differ only in paradigm (checked)
3. **Pilot Essential**: Validate workflow before committing to full runs
4. **Harness Dependency**: Need functional infrastructure for execution
5. **Documentation Valuable**: Comprehensive specs enable review and handoff

### Implementation Blocker

**Harness components** (workflows, evaluators, agents) are **scaffolded but not implemented**
- Impact: Cannot execute Steps 6-12
- Resolution: Separate harness implementation initiative
- Estimate: 3-5 days for minimal harness, 1-2 weeks for full harness

---

## Next Steps

### Immediate (Implementation Team)
1. ✅ Review design package (this README, SUMMARY.md, core specs)
2. ⏳ Approve specifications (research.md, variants, tasks)
3. ⏳ Implement minimal harness (pin-and-run, basic evaluators)
4. ⏳ Execute pilot runs (pilot-plan.md)

### Short-Term (Execution Team)
5. ⏳ Validate pilot results
6. ⏳ Execute full runs (full-runs-plan.md)
7. ⏳ Perform analysis (analysis-plan.md)
8. ⏳ Generate report (closure-plan.md)

### Long-Term (Research Team)
9. ⏳ Review findings
10. ⏳ Plan follow-up experiments (exp-002, exp-003, ...)
11. ⏳ Iterate on harness based on lessons learned

---

## Directory Structure

```
experiments/exp-001-role-vs-goal/
├── README.md                      # This file - Start here!
├── SUMMARY.md                     # Complete design package overview
├── execution-plan.md              # Original 12-step plan
├── research.md                    # Pre-registered research design (LOCKED)
│
├── tasks/
│   ├── README.md
│   ├── task-suite.md              # 6 task specifications
│   └── TASK-001/ TASK-002/ TASK-003/
│       ├── spec.json
│       └── README.md
│
├── variants/
│   ├── README.md
│   ├── role-centric.md            # Anthropomorphic variant
│   ├── goal-centric.md            # First-principles variant
│   └── parity-check.md            # Verification
│
├── evaluator-config.md            # 5 evaluators & rubrics
├── run-manifest-template.md       # Run schema & pinning
│
├── pilot-plan.md                  # Step 6: Pilot execution
├── full-runs-plan.md              # Steps 7-8: Full runs & QA
├── analysis-plan.md               # Step 9: Statistical analysis
├── closure-plan.md                # Steps 10-12: Report & close
│
├── status.md                      # Progress tracking
├── notes.md                       # Execution notes & learnings
├── suggestions.md                 # Improvement recommendations
└── need-feedback.md               # Questions & clarifications

runs/                              # (created during execution)
report/                            # (created during analysis)
```

---

## Contact & Questions

- **Design Questions**: See [need-feedback.md](need-feedback.md)
- **Implementation Questions**: Review [pilot-plan.md](pilot-plan.md) and harness requirements
- **Execution Questions**: Follow plans in order (pilot → full runs → analysis → closure)

---

## Version History

- **v1.0** (2025-12-28): Design phase complete
  - All specifications locked
  - All execution plans documented
  - Ready for implementation handoff

---

**Design Complete**: 2025-12-28  
**Next Milestone**: Pilot Execution  
**Estimated Timeline**: Design (✅ 4h) + Harness (⏳ 1-2w) + Pilot (⏳ 1d) + Runs (⏳ 1-4d) + Analysis (⏳ 1-3d)
