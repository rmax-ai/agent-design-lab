# Experiment Manifest: exp-001-role-vs-goal

**Experiment ID:** exp-001-role-vs-goal  
**Title:** Role-Centric vs Goal-Centric Agent Specification Design Patterns  
**Status:** Design Phase Complete  
**Version:** 1.0  
**Last Updated:** 2025-12-28

---

## Purpose

This manifest provides a comprehensive catalog of all canonical files bundled in the exp-001-role-vs-goal experiment. Each file is categorized, described, and linked to show its role in the experimental design and execution workflow.

---

## File Categories

### 📋 Navigation & Overview (4 files)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `README-EXPERIMENT.md` | Navigation | Quick start guide and file navigation index | ✅ Complete |
| `SUMMARY.md` | Overview | Comprehensive experiment package summary | ✅ Complete |
| `MANIFEST.md` | Catalog | This file - canonical file listing | ✅ Complete |
| `execution-plan.md` | Reference | Original 12-step execution plan (source document) | ✅ Complete |

### 🔬 Research Design (1 file)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `research.md` | Pre-registration | Hypotheses (H1-H5), metrics (9 total), analysis plan, locked before first run | 🔒 Locked |

### 📝 Task Specifications (13 files)

**Task Suite Index:**
- `tasks/task-suite.md` - Overview of all 6 tasks with categories and complexity

**Individual Task Specifications:**

| Task ID | Files | Description | Complexity |
|---------|-------|-------------|------------|
| TASK-001 | `tasks/TASK-001/README.md`<br>`tasks/TASK-001/spec.json` | Simple File Creation - Basic file operations | Low |
| TASK-002 | `tasks/TASK-002/spec.json` | Multi-File Read and Summarize - Information synthesis | Medium |
| TASK-003 | `tasks/TASK-003/spec.json` | Constrained File Edit - Precision under constraints | Medium |
| TASK-004 | `tasks/TASK-004/README.md`<br>`tasks/TASK-004/spec.json` | Error Recovery - Handling malformed inputs | Medium |
| TASK-005 | `tasks/TASK-005/README.md`<br>`tasks/TASK-005/spec.json` | Tool Composition - Multi-tool orchestration | High |
| TASK-006 | `tasks/TASK-006/README.md`<br>`tasks/TASK-006/spec.json` | Specification Ambiguity Test - Clarification behavior | Medium |

**Supporting:**
- `tasks/README.md` - Task directory overview

**Total:** 13 files (1 suite index + 6 tasks × 2 files each)

### 🎭 Variant Specifications (4 files)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `variants/role-centric.md` | Variant Spec | Anthropomorphic, persona-based agent specification | ✅ Complete |
| `variants/goal-centric.md` | Variant Spec | First-principles, objective-based agent specification | ✅ Complete |
| `variants/parity-check.md` | Verification | Parity verification proving only paradigm differs | ✅ Verified |
| `variants/README.md` | Overview | Variant directory overview | ✅ Complete |

### 📊 Evaluation Infrastructure (1 file)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `evaluator-config.md` | Configuration | 5 evaluators with scoring rubrics and scorecard schema | ✅ Complete |

**Evaluators Defined:**
1. Task Success Evaluator (binary, primary metric)
2. Constraint Adherence Evaluator (0-100 scale)
3. Runtime Evaluator (milliseconds)
4. Clarification Counter (integer count)
5. Reproducibility Evaluator (hash comparison)

### 🗺️ Execution Plans (4 files)

| File | Phase | Description | Status |
|------|-------|-------------|--------|
| `pilot-plan.md` | Step 6 | 4 pilot runs (2 tasks × 2 variants) with validation procedures | ✅ Complete |
| `full-runs-plan.md` | Steps 7-8 | 180 full runs (6 tasks × 15 pairs × 2 variants) with QA | ✅ Complete |
| `analysis-plan.md` | Step 9 | Statistical analysis workflow (paired t-tests, visualizations) | ✅ Complete |
| `closure-plan.md` | Steps 10-12 | Reporting, reproducibility verification, archiving | ✅ Complete |

### 📐 Templates & Schemas (1 file)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `run-manifest-template.md` | Template | JSON schema for run manifests with pinning strategy | ✅ Complete |

### 📈 Tracking & Metadata (4 files)

| File | Purpose | Description | Status |
|------|---------|-------------|--------|
| `status.md` | Progress | Execution progress checklist (all 12 steps tracked) | ✅ Complete |
| `notes.md` | Documentation | Detailed execution notes and learnings | ✅ Complete |
| `suggestions.md` | Improvements | 10+ process improvement recommendations | ✅ Complete |
| `need-feedback.md` | Questions | Implementation questions requiring clarification | ✅ Complete |

### 🔍 Reflections & Roadmap (2 files)

| File | Type | Description | Status |
|------|------|-------------|--------|
| `REFLECTIONS.md` | Retrospective | System improvement recommendations from execution experience | ✅ Complete |
| `NEXT-STEPS.md` | Roadmap | Prioritized action plan from design to execution (4-week timeline) | ✅ Complete |

### 🐍 Analysis Scripts (4 files)

**Location:** `analysis/`

| Script | Purpose | Dependencies | CLI |
|--------|---------|--------------|-----|
| `verify_sample_size.py` | Check minimum sample requirements (n≥10 per task) | Python 3.7+ | ✅ Yes |
| `compute_aggregates.py` | Calculate summary statistics per variant | numpy, pandas | ✅ Yes |
| `test_h1_task_success.py` | Perform paired t-test for primary hypothesis | scipy.stats | ✅ Yes |
| `bonferroni_correction.py` | Apply multiple comparison correction (α/5) | scipy.stats | ✅ Yes |

**All scripts are:**
- Executable (`chmod +x`)
- Self-documented with `--help`
- Implement algorithms from analysis-plan.md

---

## Harness Components

### 🔧 Harness Evaluators (6 files)

**Location:** `/harness/evaluators/`

| Script | Evaluator | Input | Output | Status |
|--------|-----------|-------|--------|--------|
| `task_success.py` | Task Success | run_dir, spec.json | Binary success + justification | ✅ Implemented |
| `constraint_adherence.py` | Constraint Adherence | run_dir, constraints | Score 0-100 + violations list | ✅ Implemented |
| `runtime.py` | Runtime | execution logs | Milliseconds + breakdown | ✅ Implemented |
| `clarification_counter.py` | Clarification Counter | conversation logs | Integer count + patterns | ✅ Implemented |
| `reproducibility.py` | Reproducibility | run1_dir, run2_dir | Binary match + hash | ✅ Implemented |
| `README.md` | Documentation | Overview | - | ✅ Complete |

### ⚙️ Harness Workflows (5 files)

**Location:** `/harness/workflows/`

| Script | Workflow | Purpose | Usage | Status |
|--------|----------|---------|-------|--------|
| `validate-manifest.py` | Pre-run Validation | Schema validation, pin verification | `./validate-manifest.py <manifest.json>` | ✅ Implemented |
| `evaluate.py` | Evaluation Dispatch | Orchestrate all evaluators, generate scorecard | `./evaluate.py <run_dir>` | ✅ Implemented |
| `verify-pairing.py` | Pairing Verification | Verify paired runs have identical inputs | `./verify-pairing.py <run1> <run2>` | ✅ Implemented |
| `lock-run.sh` | Immutability Marker | Mark run as immutable post-evaluation | `./lock-run.sh <run_dir>` | ✅ Implemented |
| `README.md` | Documentation | Workflow overview | - | ✅ Complete |

### 📂 Harness Supporting Directories

**Location:** `/harness/`

| Directory | Purpose | Status |
|-----------|---------|--------|
| `agents/` | Agent runtime environments (scaffolded) | 🚧 To be implemented |
| `schemas/` | JSON schemas for manifests and scorecards (scaffolded) | 🚧 To be implemented |
| `skills/` | Reusable skill modules (scaffolded) | 🚧 To be implemented |

**Note:** These directories contain README.md placeholders but require implementation before execution phase.

---

## Runtime Artifact Directories

### 📁 Directory Structure

| Directory | Purpose | Populated By | Status |
|-----------|---------|--------------|--------|
| `runs/` | Experiment run outputs | Harness execution | 🔜 Runtime |
| `report/` | Final experiment reports | Analysis scripts | 🔜 Post-analysis |

**Contents (planned):**
- `runs/` - Individual run directories with manifests, logs, scorecards, outputs
- `report/` - Comparative report, visualizations, statistical results, reproducibility verification

**Note:** These directories exist with README.md files but will be populated during execution.

---

## File Statistics

### By Category

| Category | File Count | Status |
|----------|------------|--------|
| Navigation & Overview | 4 | ✅ Complete |
| Research Design | 1 | 🔒 Locked |
| Task Specifications | 13 | ✅ Complete |
| Variant Specifications | 4 | ✅ Complete |
| Evaluation Infrastructure | 1 | ✅ Complete |
| Execution Plans | 4 | ✅ Complete |
| Templates & Schemas | 1 | ✅ Complete |
| Tracking & Metadata | 4 | ✅ Complete |
| Reflections & Roadmap | 2 | ✅ Complete |
| Analysis Scripts | 4 | ✅ Implemented |
| Harness Evaluators | 6 | ✅ Implemented |
| Harness Workflows | 5 | ✅ Implemented |
| **TOTAL DESIGN FILES** | **49** | **✅ Complete** |

### By Type

| Type | Count | Extensions |
|------|-------|-----------|
| Documentation | 32 | `.md` |
| Specifications | 6 | `.json` |
| Python Scripts | 13 | `.py` |
| Bash Scripts | 1 | `.sh` |
| **TOTAL** | **52** | - |

### By Status

| Status | Count | Percentage |
|--------|-------|-----------|
| ✅ Complete | 46 | 88.5% |
| 🔒 Locked (Pre-registration) | 1 | 1.9% |
| 🚧 To be implemented | 3 | 5.8% |
| 🔜 Runtime artifacts | 2 | 3.8% |
| **TOTAL** | **52** | **100%** |

---

## Dependency Graph

### Design Phase Dependencies

```
execution-plan.md (source)
    ↓
research.md (Step 1: hypotheses, metrics, analysis plan)
    ↓
task-suite.md (Step 2: 6 tasks defined)
    ↓
variants/*.md (Step 3: role-centric, goal-centric, parity)
    ↓
evaluator-config.md (Step 4: 5 evaluators, rubrics)
    ↓
run-manifest-template.md (Step 5: schema, pinning)
    ↓
pilot-plan.md (Step 6: 4 pilot runs)
    ↓
full-runs-plan.md (Steps 7-8: 180 runs, QA)
    ↓
analysis-plan.md (Step 9: statistical tests)
    ↓
closure-plan.md (Steps 10-12: report, archive)
```

### Implementation Dependencies

```
evaluator-config.md
    ↓
harness/evaluators/*.py (5 evaluators)

run-manifest-template.md
    ↓
harness/workflows/validate-manifest.py

analysis-plan.md
    ↓
experiments/exp-001-role-vs-goal/analysis/*.py (4 scripts)
```

### Execution Phase Dependencies (Planned)

```
pilot-plan.md + tasks/ + variants/
    ↓
runs/ (4 pilot runs)
    ↓
harness/workflows/evaluate.py
    ↓
Go/No-Go Decision
    ↓
full-runs-plan.md
    ↓
runs/ (180 full runs)
    ↓
analysis/*.py
    ↓
report/ (final outputs)
```

---

## Immutability Contract

### Locked Files (Pre-registration)

Once the first pinned run is executed, the following files **MUST NOT** be modified:

1. **research.md** - Pre-registered hypotheses, metrics, analysis plan (already locked)
2. **tasks/task-suite.md** + all task specs - Task definitions (frozen at v1.0)
3. **variants/*.md** - Variant specifications (frozen post-parity-check)
4. **evaluator-config.md** - Evaluator definitions and rubrics

**Rationale:** Scientific rigor requires pre-registration before data collection to prevent p-hacking and HARKing (Hypothesizing After Results are Known).

### Modifiable Files

These files may be updated during execution:

- `status.md` - Progress tracking (continuously updated)
- `notes.md` - Execution observations (continuously updated)
- `suggestions.md` - Process improvements (may add items)
- `need-feedback.md` - Questions (may add items)
- All tracking and metadata files

---

## Version History

| Version | Date | Description | Files Changed |
|---------|------|-------------|---------------|
| 1.0 | 2025-12-28 | Initial design package complete | All 49 design files created |

---

## Checksums (SHA-256)

For reproducibility and integrity verification, checksums of all locked files:

```bash
# Generate checksums for locked files:
cd experiments/exp-001-role-vs-goal
sha256sum research.md tasks/task-suite.md tasks/TASK-*/spec.json \
  variants/role-centric.md variants/goal-centric.md \
  variants/parity-check.md evaluator-config.md > CHECKSUMS.txt
```

**Note:** Checksums should be generated and committed before first pilot run.

---

## Usage Guidelines

### For Experiment Executors

1. **Start here:** Read `README-EXPERIMENT.md` for navigation
2. **Understand design:** Read `SUMMARY.md` for complete overview
3. **Follow roadmap:** Use `NEXT-STEPS.md` for execution sequence
4. **Verify completeness:** Use this MANIFEST to ensure all files present
5. **Track progress:** Update `status.md` as you complete tasks

### For Peer Reviewers

1. **Review research design:** `research.md` (hypotheses, metrics, analysis plan)
2. **Verify tasks:** `tasks/task-suite.md` + individual specs
3. **Check parity:** `variants/parity-check.md` (only paradigm differs)
4. **Validate evaluators:** `evaluator-config.md` (rubrics are clear)
5. **Assess feasibility:** `NEXT-STEPS.md` (timeline and resources reasonable)

### For Future Experiments

1. **Use as template:** This MANIFEST structure can be adapted for other experiments
2. **Leverage scripts:** Analysis and harness scripts are reusable
3. **Learn from reflections:** `REFLECTIONS.md` contains process improvements
4. **Follow patterns:** Execution plan structure proven effective

---

## Quick Reference Commands

### Validate Experiment Structure

```bash
# Check all design files present
cd experiments/exp-001-role-vs-goal
ls -la | wc -l  # Should be 20+ items

# Check task specs
ls tasks/TASK-*/spec.json | wc -l  # Should be 6

# Check harness implementations
ls /harness/evaluators/*.py | wc -l  # Should be 5
ls /harness/workflows/*.py | wc -l  # Should be 3

# Check analysis scripts
ls analysis/*.py | wc -l  # Should be 4
```

### Verify Script Functionality

```bash
# Test all scripts have CLI help
cd analysis
for script in *.py; do
  ./$script --help || echo "FAIL: $script"
done

cd ../../harness/workflows
for script in *.py; do
  ./$script --help || echo "FAIL: $script"
done
```

### Generate Integrity Report

```bash
# Create checksums for version control
cd experiments/exp-001-role-vs-goal
find . -type f \( -name "*.md" -o -name "*.json" -o -name "*.py" -o -name "*.sh" \) \
  | sort | xargs sha256sum > INTEGRITY-MANIFEST.txt
```

---

## Contact & Support

**Experiment Owner:** Research Team  
**Documentation Date:** 2025-12-28  
**Next Review:** Before pilot execution (Week 1)

**For questions or issues:**
1. Check `need-feedback.md` for known questions
2. Review `REFLECTIONS.md` for common pitfalls
3. Consult `NEXT-STEPS.md` for execution guidance

---

## Appendix: File Tree

```
experiments/exp-001-role-vs-goal/
├── MANIFEST.md                    # This file
├── README-EXPERIMENT.md           # Navigation guide
├── SUMMARY.md                     # Complete overview
├── NEXT-STEPS.md                  # Execution roadmap
├── REFLECTIONS.md                 # System improvements
├── execution-plan.md              # Original source plan
├── research.md                    # Pre-registration (LOCKED)
├── status.md                      # Progress tracking
├── notes.md                       # Execution notes
├── suggestions.md                 # Improvements
├── need-feedback.md               # Questions
├── evaluator-config.md            # 5 evaluators + rubrics
├── run-manifest-template.md       # Run schema
├── pilot-plan.md                  # Step 6 plan
├── full-runs-plan.md              # Steps 7-8 plan
├── analysis-plan.md               # Step 9 plan
├── closure-plan.md                # Steps 10-12 plan
├── analysis/
│   ├── verify_sample_size.py     # Sample size checker
│   ├── compute_aggregates.py     # Statistics calculator
│   ├── test_h1_task_success.py   # Paired t-test
│   └── bonferroni_correction.py  # Multiple comparison
├── tasks/
│   ├── README.md                  # Task overview
│   ├── task-suite.md              # Suite definition
│   ├── TASK-001/
│   │   ├── README.md
│   │   └── spec.json
│   ├── TASK-002/
│   │   └── spec.json
│   ├── TASK-003/
│   │   └── spec.json
│   ├── TASK-004/
│   │   ├── README.md
│   │   └── spec.json
│   ├── TASK-005/
│   │   ├── README.md
│   │   └── spec.json
│   └── TASK-006/
│       ├── README.md
│       └── spec.json
├── variants/
│   ├── README.md                  # Variant overview
│   ├── role-centric.md            # Anthropomorphic spec
│   ├── goal-centric.md            # First-principles spec
│   └── parity-check.md            # Parity verification
├── runs/
│   └── README.md                  # Runtime artifacts (to be populated)
└── report/
    └── README.md                  # Final reports (to be populated)

/harness/
├── README.md                      # Harness overview
├── evaluators/
│   ├── README.md
│   ├── task_success.py           # Binary success evaluator
│   ├── constraint_adherence.py   # Constraint checker
│   ├── runtime.py                # Runtime metrics
│   ├── clarification_counter.py  # Clarification detector
│   └── reproducibility.py        # Cross-run comparison
├── workflows/
│   ├── README.md
│   ├── validate-manifest.py      # Pre-run validation
│   ├── evaluate.py               # Evaluation dispatcher
│   ├── verify-pairing.py         # Pairing verification
│   └── lock-run.sh               # Immutability marker
├── agents/
│   └── README.md                 # (scaffolded)
├── schemas/
│   └── README.md                 # (scaffolded)
└── skills/
    └── README.md                 # (scaffolded)
```

**Total:** 52 canonical files across 49 design documents and 13 scripts.

---

**End of Manifest**
