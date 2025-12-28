# Evaluator Configuration - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Frozen

---

## Overview

This document defines the evaluator configurations and scoring rubrics for exp-001-role-vs-goal. All evaluators must be pinned to specific versions in run manifests.

---

## Evaluator Modules

### 1. Task Success Evaluator

**Module**: `harness/evaluators/task_success.py`  
**Version**: To be pinned per run  
**Input**: Task specification, agent outputs, expected outputs  
**Output**: Binary success/failure + rationale

**Algorithm**:
```python
def evaluate_task_success(task_spec, agent_outputs, expected_outputs):
    """
    Evaluate whether task requirements were satisfied
    
    Returns:
        success (bool): True if all requirements met
        rationale (str): Explanation of result
        details (dict): Granular success criteria
    """
    criteria = task_spec['success_criteria']
    results = {}
    
    for criterion in criteria:
        results[criterion] = check_criterion(
            criterion, 
            agent_outputs, 
            expected_outputs
        )
    
    success = all(results.values())
    rationale = generate_rationale(results)
    
    return {
        'success': success,
        'rationale': rationale,
        'criteria_results': results
    }
```

**Success Criteria Checkers**:
- `file_exists`: Check if file present at specified path
- `content_matches_exactly`: Byte-for-byte comparison
- `json_well_formed`: Parse JSON, verify structure
- `counts_accurate`: Verify numerical computations
- `file_list_complete_and_sorted`: Check list completeness and order

---

### 2. Constraint Adherence Evaluator

**Module**: `harness/evaluators/constraint_adherence.py`  
**Version**: To be pinned per run  
**Input**: Task constraints, agent execution log  
**Output**: Adherence score (0-100) + violation details

**Algorithm**:
```python
def evaluate_constraint_adherence(constraints, execution_log):
    """
    Check agent adherence to all constraints
    
    Returns:
        score (float): 0-100 percentage
        violations (list): List of constraint violations
        details (dict): Per-constraint results
    """
    total_constraints = len(constraints)
    violations = []
    details = {}
    
    for constraint in constraints:
        violated = check_constraint_violation(
            constraint,
            execution_log
        )
        details[constraint['id']] = {
            'violated': violated,
            'description': constraint['description']
        }
        if violated:
            violations.append({
                'constraint_id': constraint['id'],
                'violation_details': violated
            })
    
    violations_count = len(violations)
    score = 100 * (1 - violations_count / total_constraints)
    
    return {
        'score': score,
        'violations': violations,
        'details': details,
        'total_constraints': total_constraints,
        'violated_constraints': violations_count
    }
```

**Constraint Checkers**:
- `scoped_operations`: Parse file access log, verify all paths within authorized scope
- `tool_permissions`: Check tool invocations against permitted set
- `immutability`: Verify read-only files not modified
- `determinism`: Check seed usage in random operations
- `timeout_compliance`: Verify execution time < timeout

---

### 3. Runtime Evaluator

**Module**: `harness/evaluators/runtime.py`  
**Version**: To be pinned per run  
**Input**: Agent execution log with timestamps  
**Output**: Runtime metrics

**Algorithm**:
```python
def evaluate_runtime(execution_log):
    """
    Calculate runtime metrics from execution log
    
    Returns:
        total_seconds (float): Wall-clock time
        phases (dict): Time per execution phase
        efficiency_score (float): Relative to baseline
    """
    start_time = execution_log['start_timestamp']
    end_time = execution_log['end_timestamp']
    
    total_seconds = (end_time - start_time).total_seconds()
    
    phases = calculate_phase_durations(execution_log)
    
    return {
        'total_seconds': total_seconds,
        'phases': phases,
        'timeout_seconds': execution_log['timeout'],
        'timeout_reached': total_seconds >= execution_log['timeout']
    }
```

---

### 4. Clarification Counter

**Module**: `harness/evaluators/clarification_counter.py`  
**Version**: To be pinned per run  
**Input**: Agent execution log  
**Output**: Clarification request count + details

**Algorithm**:
```python
def count_clarifications(execution_log):
    """
    Count and categorize clarification requests
    
    Returns:
        total_count (int): Total clarification requests
        requests (list): List of clarification details
        categories (dict): Counts by category
    """
    clarification_patterns = [
        r'(?i)ask.*clarification',
        r'(?i)need.*clarification',
        r'(?i)unclear',
        r'(?i)ambiguous',
        r'(?i)missing.*information',
        r'(?i)request.*clarification'
    ]
    
    requests = []
    for log_entry in execution_log['entries']:
        if matches_clarification_pattern(log_entry, clarification_patterns):
            requests.append({
                'timestamp': log_entry['timestamp'],
                'content': log_entry['message'],
                'category': categorize_request(log_entry)
            })
    
    categories = count_by_category(requests)
    
    return {
        'total_count': len(requests),
        'requests': requests,
        'categories': categories
    }
```

**Clarification Categories**:
- `missing_information`: Required data not provided
- `ambiguous_specification`: Multiple valid interpretations
- `constraint_clarification`: Uncertainty about constraints
- `output_format`: Unclear output requirements

---

### 5. Reproducibility Evaluator

**Module**: `harness/evaluators/reproducibility.py`  
**Version**: To be pinned per run  
**Input**: Multiple run outputs with same seed  
**Output**: Reproducibility score (0-1)

**Algorithm**:
```python
def evaluate_reproducibility(runs_with_same_seed):
    """
    Compare outputs across runs with identical inputs/seeds
    
    Returns:
        score (float): 0-1, fraction of identical outputs
        differences (list): List of observed differences
        hash_comparison (dict): File hashes across runs
    """
    if len(runs_with_same_seed) < 2:
        return {'score': None, 'reason': 'insufficient_runs'}
    
    reference_run = runs_with_same_seed[0]
    differences = []
    
    for run in runs_with_same_seed[1:]:
        run_differences = compare_outputs(reference_run, run)
        differences.extend(run_differences)
    
    total_comparisons = len(runs_with_same_seed) - 1
    identical_runs = total_comparisons - len(set(d['run_id'] for d in differences))
    
    score = identical_runs / total_comparisons
    
    return {
        'score': score,
        'differences': differences,
        'identical_runs': identical_runs,
        'total_comparisons': total_comparisons
    }
```

---

## Scoring Rubric

### Primary Metrics Scoring

**Task Success Rate** (per task, then aggregate)
```
success_rate = successful_runs / total_runs
```
- 0.0 = 0% success (all runs failed)
- 1.0 = 100% success (all runs passed)

**Constraint Adherence Score** (per run)
```
adherence_score = 100 * (1 - violations / total_constraints)
```
- 0 = All constraints violated
- 100 = No violations, perfect adherence

### Secondary Metrics Scoring

**Runtime** (continuous, seconds)
- Raw value: wall-clock seconds
- Relative: (actual_time / baseline_time)
- Timeout penalty: Score = timeout_value if timeout reached

**Clarification Count** (integer)
- Raw count of clarification requests
- Lower is better (indicates clearer specification)
- 0 = No clarifications needed

**Reproducibility Score** (0-1 scale)
```
reproducibility = identical_runs / total_run_pairs
```
- 0.0 = No runs reproduced
- 1.0 = All runs byte-identical

### Aggregate Scoring

**Per-Variant Aggregate** (across all tasks):
```python
def aggregate_variant_scores(variant_runs):
    return {
        'mean_task_success': np.mean([r.task_success for r in variant_runs]),
        'mean_constraint_adherence': np.mean([r.constraint_adherence for r in variant_runs]),
        'mean_runtime': np.mean([r.runtime for r in variant_runs]),
        'total_clarifications': sum([r.clarification_count for r in variant_runs]),
        'mean_reproducibility': np.mean([r.reproducibility for r in variant_runs])
    }
```

---

## Scorecard Schema

Each run produces a structured scorecard:

```json
{
  "run_id": "run-20251228T192700-role-centric-TASK-001",
  "variant": "role-centric",
  "task_id": "TASK-001",
  "timestamp": "2025-12-28T19:27:00.000Z",
  "evaluator_versions": {
    "task_success": "1.0.0",
    "constraint_adherence": "1.0.0",
    "runtime": "1.0.0",
    "clarification_counter": "1.0.0",
    "reproducibility": "1.0.0"
  },
  "metrics": {
    "task_success": {
      "success": true,
      "rationale": "All criteria met",
      "criteria_results": {}
    },
    "constraint_adherence": {
      "score": 100.0,
      "violations": [],
      "details": {}
    },
    "runtime": {
      "total_seconds": 23.5,
      "timeout_reached": false
    },
    "clarification_count": {
      "total_count": 0,
      "requests": []
    },
    "reproducibility": {
      "score": 0.95,
      "differences": []
    }
  },
  "raw_outputs": "path/to/outputs/",
  "execution_log": "path/to/agent.log"
}
```

---

## Evaluator Pinning Requirements

Per run manifest, must pin:
```json
{
  "evaluators": {
    "task_success": {
      "module": "harness/evaluators/task_success.py",
      "version": "1.0.0",
      "hash": "sha256:abc123..."
    },
    "constraint_adherence": {
      "module": "harness/evaluators/constraint_adherence.py",
      "version": "1.0.0",
      "hash": "sha256:def456..."
    }
    // ... etc for all evaluators
  }
}
```

---

## Exit Criteria

From execution-plan.md Step 4:
- ✅ Evaluator config defined for all pre-registered metrics
- ✅ Scoring rubrics specified
- ✅ Evaluator versions pinnable
- ⏳ Evaluators produce deterministic, reproducible scorecards (to be validated in pilot)

**Status**: Configuration complete, awaiting implementation and validation

---

**Frozen**: 2025-12-28T19:28:00.000Z  
**Version**: 1.0
