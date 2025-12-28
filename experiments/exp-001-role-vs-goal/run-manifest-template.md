# Run Manifest Template - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Purpose**: Template for pinned run manifests ensuring reproducibility

---

## Manifest Schema

Each run MUST produce a manifest conforming to this schema:

```json
{
  "$schema": "https://agent-design-lab/schemas/run-manifest-v1.json",
  "manifest_version": "1.0",
  "run_id": "run-{timestamp}-{variant}-{task_id}",
  "experiment_id": "exp-001-role-vs-goal",
  "created_at": "{ISO8601 timestamp}",
  
  "pins": {
    "harness_version": "{git_commit_sha}",
    "harness_repository": "rmax-ai/agent-design-lab",
    "harness_path": "harness/",
    
    "evaluator_versions": {
      "task_success": {
        "module": "harness/evaluators/task_success.py",
        "version": "1.0.0",
        "hash": "sha256:{hash}"
      },
      "constraint_adherence": {
        "module": "harness/evaluators/constraint_adherence.py",
        "version": "1.0.0",
        "hash": "sha256:{hash}"
      },
      "runtime": {
        "module": "harness/evaluators/runtime.py",
        "version": "1.0.0",
        "hash": "sha256:{hash}"
      },
      "clarification_counter": {
        "module": "harness/evaluators/clarification_counter.py",
        "version": "1.0.0",
        "hash": "sha256:{hash}"
      },
      "reproducibility": {
        "module": "harness/evaluators/reproducibility.py",
        "version": "1.0.0",
        "hash": "sha256:{hash}"
      }
    },
    
    "tool_permission_set": {
      "file_operations": ["read", "write", "create", "delete"],
      "allowed_paths": ["/tmp/exp-test/**"],
      "forbidden_paths": ["/", "/etc/**", "/sys/**"],
      "network_access": false,
      "subprocess_spawn": false
    }
  },
  
  "variant": {
    "variant_id": "role-centric | goal-centric",
    "specification_file": "experiments/exp-001-role-vs-goal/variants/{variant_id}.md",
    "specification_hash": "sha256:{hash}",
    "paradigm": "anthropomorphic | first-principles"
  },
  
  "task": {
    "task_id": "{TASK-00X}",
    "specification_file": "experiments/exp-001-role-vs-goal/tasks/{task_id}/spec.json",
    "specification_hash": "sha256:{hash}",
    "seed": 42,
    "timeout_seconds": 60
  },
  
  "inputs": {
    "snapshot_path": "experiments/exp-001-role-vs-goal/runs/{run_id}/inputs/",
    "files": [
      {
        "path": "{relative_path}",
        "hash": "sha256:{hash}",
        "size_bytes": 1234
      }
    ]
  },
  
  "execution": {
    "started_at": "{ISO8601 timestamp}",
    "completed_at": "{ISO8601 timestamp}",
    "duration_seconds": 23.45,
    "timeout_reached": false,
    "exit_code": 0,
    "exit_reason": "success | timeout | error"
  },
  
  "outputs": {
    "path": "experiments/exp-001-role-vs-goal/runs/{run_id}/outputs/",
    "files": [
      {
        "path": "{relative_path}",
        "hash": "sha256:{hash}",
        "size_bytes": 5678
      }
    ]
  },
  
  "logs": {
    "execution_log": "experiments/exp-001-role-vs-goal/runs/{run_id}/agent.log",
    "execution_log_hash": "sha256:{hash}",
    "evaluation_log": "experiments/exp-001-role-vs-goal/runs/{run_id}/evaluation.log",
    "evaluation_log_hash": "sha256:{hash}"
  },
  
  "evaluation": {
    "scorecard_path": "experiments/exp-001-role-vs-goal/runs/{run_id}/scorecard.json",
    "scorecard_hash": "sha256:{hash}",
    "evaluated_at": "{ISO8601 timestamp}"
  },
  
  "pairing": {
    "pair_id": "pair-{timestamp}-{task_id}",
    "paired_run_id": "run-{timestamp}-{other_variant}-{task_id}",
    "is_reference_run": true
  },
  
  "immutability": {
    "locked_at": "{ISO8601 timestamp}",
    "locked": true,
    "lock_reason": "run_completed"
  },
  
  "metadata": {
    "experiment_version": "1.0",
    "pre_registration_hash": "sha256:{hash_of_research.md}",
    "task_suite_version": "1.0",
    "variant_version": "1.0",
    "notes": ""
  }
}
```

---

## Manifest Generation Workflow

### Pre-Run Phase

1. **Initialize Manifest**
   ```bash
   $ ./harness/workflows/pin-and-run --init \
       --experiment exp-001-role-vs-goal \
       --variant role-centric \
       --task TASK-001
   ```
   
   Generates:
   - run_id (timestamp-based)
   - pins harness version (current git SHA)
   - pins evaluator versions (current versions + hashes)
   - pins variant specification (file + hash)
   - pins task specification (file + hash)
   - snapshots input files

2. **Validate Manifest**
   ```bash
   $ ./harness/workflows/validate-manifest \
       --manifest runs/{run_id}/manifest.json
   ```
   
   Checks:
   - Schema compliance
   - All pins present and valid
   - No floating versions
   - Hashes computed correctly
   - Paths exist and accessible

### Run Phase

3. **Execute Run**
   ```bash
   $ ./harness/workflows/pin-and-run --execute \
       --manifest runs/{run_id}/manifest.json
   ```
   
   - Loads variant specification
   - Loads task specification
   - Executes agent with pinned configuration
   - Logs all operations
   - Captures outputs
   - Updates manifest with execution metadata

4. **Evaluate Run**
   ```bash
   $ ./harness/workflows/evaluate \
       --manifest runs/{run_id}/manifest.json
   ```
   
   - Loads pinned evaluators
   - Runs all evaluation modules
   - Generates scorecard
   - Updates manifest with evaluation metadata

### Post-Run Phase

5. **Lock Manifest**
   ```bash
   $ ./harness/workflows/lock-run \
       --manifest runs/{run_id}/manifest.json
   ```
   
   - Marks run as immutable
   - Computes final hashes
   - Sets lock timestamp
   - Appends to run log

---

## Pre-Run Validation Script

```python
#!/usr/bin/env python3
"""
Pre-run manifest validator

Ensures manifest meets all requirements before execution
"""

import json
import hashlib
from pathlib import Path

def validate_manifest(manifest_path):
    """
    Validate run manifest before execution
    
    Returns:
        valid (bool): True if manifest passes all checks
        errors (list): List of validation errors
    """
    errors = []
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    # Check schema version
    if manifest.get('manifest_version') != '1.0':
        errors.append('Invalid manifest version')
    
    # Check all pins present
    required_pins = [
        'harness_version',
        'evaluator_versions',
        'tool_permission_set'
    ]
    for pin in required_pins:
        if pin not in manifest.get('pins', {}):
            errors.append(f'Missing pin: {pin}')
    
    # Check no floating versions
    for evaluator, config in manifest['pins']['evaluator_versions'].items():
        if not config.get('version'):
            errors.append(f'Evaluator {evaluator} has no version pin')
        if not config.get('hash'):
            errors.append(f'Evaluator {evaluator} has no hash pin')
    
    # Check variant specification exists
    variant_spec = Path(manifest['variant']['specification_file'])
    if not variant_spec.exists():
        errors.append(f'Variant specification not found: {variant_spec}')
    
    # Check task specification exists
    task_spec = Path(manifest['task']['specification_file'])
    if not task_spec.exists():
        errors.append(f'Task specification not found: {task_spec}')
    
    # Check input snapshots
    input_path = Path(manifest['inputs']['snapshot_path'])
    if not input_path.exists():
        errors.append(f'Input snapshot path not found: {input_path}')
    
    valid = len(errors) == 0
    
    return {
        'valid': valid,
        'errors': errors,
        'warnings': []
    }

if __name__ == '__main__':
    import sys
    result = validate_manifest(sys.argv[1])
    
    if not result['valid']:
        print('VALIDATION FAILED')
        for error in result['errors']:
            print(f'  ERROR: {error}')
        sys.exit(1)
    else:
        print('VALIDATION PASSED')
        sys.exit(0)
```

---

## Manifest Immutability Contract

### Immutability Rules

1. **Before Execution**: Manifest is mutable
   - Can update pins
   - Can modify configuration
   - Must re-validate after changes

2. **During Execution**: Manifest is read-only
   - Only execution metadata updated
   - Pins MUST NOT change
   - Inputs MUST NOT change

3. **After Completion**: Manifest is immutable
   - `immutability.locked` = true
   - `immutability.locked_at` timestamp set
   - Any modification requires new run with new run_id

### Correction Policy

If error discovered in completed run:
1. Document error in experiments/exp-001-role-vs-goal/runs/corrections.md
2. Create new run with corrected configuration
3. Mark original run with error flag (but keep immutable)
4. Link correction run to original run via metadata

---

## Pairing Strategy

### Paired Run Execution

Each task executed by both variants with identical configuration:

```json
{
  "pair_id": "pair-20251228T192900-TASK-001",
  "runs": [
    {
      "run_id": "run-20251228T192900-role-centric-TASK-001",
      "variant": "role-centric",
      "execution_order": 1
    },
    {
      "run_id": "run-20251228T192905-goal-centric-TASK-001",
      "variant": "goal-centric",
      "execution_order": 2
    }
  ],
  "pairing_requirements": {
    "identical_task": true,
    "identical_inputs": true,
    "identical_seed": true,
    "identical_timeout": true,
    "identical_permissions": true,
    "execution_order": "randomized"
  }
}
```

### Interleaving Policy

To minimize temporal bias:
- Randomize execution order within pairs
- Don't run all role-centric first, then all goal-centric
- Interleave: R, G, G, R, R, G, ... (randomized)

---

## Exit Criteria

From execution-plan.md Step 5:
- ✅ Run manifest template created
- ✅ Pinning requirements specified
- ✅ Pre-run validator defined
- ⏳ Manifest passes schema validation (to be implemented and tested)
- ⏳ Pre-run checks implemented (to be implemented)

**Status**: Template complete, awaiting implementation and testing in pilot runs

---

**Version**: 1.0  
**Frozen**: 2025-12-28T19:29:00.000Z
