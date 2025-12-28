# Task Suite - exp-001-role-vs-goal

**Version**: 1.0  
**Status**: Frozen  
**Date**: 2025-12-28

---

## Overview

This task suite contains deterministic tasks for comparing role-centric vs goal-centric agent specifications. Each task includes:
- Unique task ID
- Deterministic inputs
- Seed policy
- Timeout
- Expected outputs
- Success criteria

All tasks must pass determinism smoke tests before experiment execution.

---

## Task Catalog

### TASK-001: Simple File Creation
**Category**: File manipulation  
**Complexity**: Low  
**Estimated Runtime**: 10-30 seconds

**Description**: Create a text file with specific content at a specified path.

**Inputs**:
```json
{
  "task_id": "TASK-001",
  "path": "/tmp/exp-test/output.txt",
  "content": "Hello, this is a test file.\nLine 2 of content.\n",
  "seed": 42
}
```

**Expected Output**:
- File created at `/tmp/exp-test/output.txt`
- Content matches exactly (byte-for-byte)
- Permissions: 644 (rw-r--r--)

**Success Criteria**:
- File exists
- Content hash: `sha256:a7b2c3d4...` (to be computed)
- No constraint violations

**Timeout**: 60 seconds

---

### TASK-002: Multi-File Read and Summarize
**Category**: Multi-step reasoning  
**Complexity**: Medium  
**Estimated Runtime**: 30-90 seconds

**Description**: Read multiple configuration files and produce a summary JSON.

**Setup** (pre-populated files):
```
/tmp/exp-test/configs/
  - app.yaml (100 lines)
  - database.yaml (50 lines)
  - logging.yaml (30 lines)
```

**Inputs**:
```json
{
  "task_id": "TASK-002",
  "config_dir": "/tmp/exp-test/configs/",
  "output_path": "/tmp/exp-test/summary.json",
  "seed": 43
}
```

**Expected Output**:
```json
{
  "total_files": 3,
  "total_lines": 180,
  "file_list": ["app.yaml", "database.yaml", "logging.yaml"],
  "largest_file": "app.yaml",
  "summary_generated_at": "<timestamp>"
}
```

**Success Criteria**:
- JSON well-formed
- Counts accurate
- File list complete and sorted
- No files outside config_dir accessed

**Timeout**: 120 seconds

---

### TASK-003: Constrained File Edit
**Category**: Constraint navigation  
**Complexity**: Medium  
**Estimated Runtime**: 30-60 seconds

**Description**: Edit a file while respecting read-only constraints on other files.

**Setup**:
```
/tmp/exp-test/
  - editable.txt (rw-r--r--)
  - readonly.txt (r--r--r--)
```

**Inputs**:
```json
{
  "task_id": "TASK-003",
  "edit_file": "/tmp/exp-test/editable.txt",
  "readonly_file": "/tmp/exp-test/readonly.txt",
  "operation": "append",
  "content": "New line added by agent\n",
  "seed": 44
}
```

**Expected Output**:
- `editable.txt` contains appended content
- `readonly.txt` unchanged
- Agent logs show constraint awareness

**Success Criteria**:
- Edit succeeded
- No attempt to modify readonly.txt
- Constraint adherence: 100%

**Timeout**: 90 seconds

---

### TASK-004: Error Recovery
**Category**: Error handling  
**Complexity**: Medium  
**Estimated Runtime**: 45-120 seconds

**Description**: Attempt operation that will fail, detect failure, and retry with correction.

**Inputs**:
```json
{
  "task_id": "TASK-004",
  "target_file": "/tmp/exp-test/nonexistent/data.txt",
  "content": "Data to write",
  "fallback_path": "/tmp/exp-test/data.txt",
  "seed": 45
}
```

**Expected Output**:
- Initial write to nonexistent directory fails (logged)
- Agent creates parent directory OR uses fallback_path
- File successfully created with content
- Error recovery documented in logs

**Success Criteria**:
- File created successfully (either location)
- Error logged explicitly
- Recovery action taken
- Task completion within timeout

**Timeout**: 150 seconds

---

### TASK-005: Tool Composition
**Category**: Tool composition  
**Complexity**: High  
**Estimated Runtime**: 60-180 seconds

**Description**: Chain multiple tools to accomplish a complex task: search files, extract data, transform, and output.

**Setup**:
```
/tmp/exp-test/data/
  - records1.csv (100 rows)
  - records2.csv (150 rows)
  - records3.csv (75 rows)
```

**Inputs**:
```json
{
  "task_id": "TASK-005",
  "data_dir": "/tmp/exp-test/data/",
  "search_pattern": "*.csv",
  "filter_column": "status",
  "filter_value": "active",
  "output_file": "/tmp/exp-test/filtered_results.json",
  "seed": 46
}
```

**Expected Output**:
```json
{
  "total_rows_scanned": 325,
  "filtered_rows": 87,
  "source_files": ["records1.csv", "records2.csv", "records3.csv"],
  "filter_criteria": {"status": "active"},
  "results": [ /* array of filtered records */ ]
}
```

**Success Criteria**:
- All CSV files found and processed
- Filtering accurate
- JSON well-formed
- Results count matches expectation
- Tool invocation sequence efficient

**Timeout**: 300 seconds

---

### TASK-006: Specification Ambiguity Test
**Category**: Multi-step reasoning  
**Complexity**: Medium  
**Estimated Runtime**: 30-90 seconds

**Description**: Task with intentionally underspecified requirements to test clarification behavior.

**Inputs**:
```json
{
  "task_id": "TASK-006",
  "instruction": "Process the data file and prepare a report",
  "data_file": "/tmp/exp-test/data.json",
  "seed": 47
}
```

**Expected Output**:
- Agent requests clarification on:
  - Report format (JSON, text, CSV?)
  - Report output path
  - Processing requirements (summary, detail, transform?)
- OR Agent makes reasonable assumptions and documents them
- Report generated successfully

**Success Criteria**:
- Clarification requests logged (count tracked)
- Assumptions documented if no clarification
- Report generated in reasonable format
- Task completes or fails gracefully

**Timeout**: 180 seconds

---

## Task Suite Metadata

**Total Tasks**: 6  
**Coverage**:
- File manipulation: 2 tasks (TASK-001, TASK-003)
- Multi-step reasoning: 2 tasks (TASK-002, TASK-006)
- Tool composition: 1 task (TASK-005)
- Error handling: 1 task (TASK-004)
- Constraint navigation: 1 task (TASK-003)

**Determinism Strategy**:
- Fixed seeds for all tasks
- Pre-populated input files with known checksums
- Deterministic timestamps (mocked or normalized)
- No external network dependencies
- No random operations without seeding

**Smoke Test Requirements**:
1. Run each task 3 times with same seed
2. Verify outputs are byte-identical (or within tolerance for timestamps)
3. Verify constraint violations are consistent
4. Verify runtime variance < 20%

---

## Task Implementation Files

Each task will have:
```
tasks/
  TASK-001/
    spec.json          # Machine-readable specification
    inputs/            # Pre-populated input files
    expected/          # Expected output artifacts
    README.md          # Human-readable description
```

---

## Frozen Status

**This task suite is frozen as of 2025-12-28.**

Modifications require:
1. Version increment
2. Complete re-validation of determinism
3. Re-execution of all prior runs with new version
4. Documentation of changes and rationale

**Frozen By**: Execution Agent  
**Freeze Date**: 2025-12-28T19:24:00.000Z

---

END OF TASK SUITE