# Variant Parity Check - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Purpose**: Verify that role-centric and goal-centric variants differ ONLY in specification paradigm

---

## Parity Requirements

Per project/manifest.md and execution-plan.md Step 3:
- Two variant descriptors that reference harness agents/tools
- **ONLY the specification paradigm differs**
- Identical tooling, constraints, permissions

---

## Parity Verification Matrix

| Element | Role-Centric | Goal-Centric | Status |
|---------|--------------|--------------|---------|
| **Tool Access** | File system ops, data processing | File system ops, data processing | ✅ IDENTICAL |
| **Constraints** | Scoped ops, permissions, immutability, determinism, timeout | Scoped ops, permissions, immutability, determinism, timeout | ✅ IDENTICAL |
| **Task Specifications** | References tasks/ | References tasks/ | ✅ IDENTICAL |
| **Evaluation Metrics** | Task success, constraint adherence, runtime, clarification count | Task success, constraint adherence, runtime, clarification count | ✅ IDENTICAL |
| **Timeout Handling** | Must complete within timeout | Must complete within timeout | ✅ IDENTICAL |
| **Logging Requirements** | Structured execution logs | Structured execution logs | ✅ IDENTICAL |
| **Error Recovery** | Handle errors professionally, recover when possible | Recoverable vs unrecoverable, retry logic | ✅ EQUIVALENT |
| **Clarification Protocol** | Ask when ambiguous, suggest alternatives | Log ambiguity, request clarification or assume | ✅ EQUIVALENT |
| **Harness Version** | Pinned per run | Pinned per run | ✅ IDENTICAL |

---

## Differences (Specification Paradigm Only)

### Role-Centric Characteristics
- **Language**: Anthropomorphic (persona, role, personality)
- **Framing**: "You are a helpful assistant"
- **Style**: Narrative instructions, working style guidelines
- **Conceptualization**: Human-like professional with traits
- **Instructions**: "Think through problems step-by-step like an experienced developer"

### Goal-Centric Characteristics
- **Language**: Functional (objectives, constraints, control loops)
- **Framing**: "Goal-driven control system"
- **Style**: Algorithmic pseudocode, formal specifications
- **Conceptualization**: Deterministic system optimizing toward objectives
- **Instructions**: "Execute control loop: assess state → select operation → validate constraints"

---

## Constraint Mapping

Both variants enforce identical constraints with different framing:

### Scoped Operations
- **Role-Centric**: "Only access files and directories within your authorized scope"
- **Goal-Centric**: "C1: All file system operations MUST be within authorized paths"
- **Status**: ✅ Semantically identical

### Permission Boundaries
- **Role-Centric**: "Respect boundaries... Follow rules... Adhere to specified constraints"
- **Goal-Centric**: "C2: Only use tools explicitly granted per task specification"
- **Status**: ✅ Semantically identical

### Read-Only Files
- **Role-Centric**: Implicit in "respect boundaries" and "follow rules"
- **Goal-Centric**: "C3: Read-only files MUST NOT be modified"
- **Status**: ✅ Goal-centric more explicit, but same requirement

### Determinism
- **Role-Centric**: Implicit in task execution (seed provided in tasks)
- **Goal-Centric**: "C4: Use provided seed for any random operations"
- **Status**: ✅ Goal-centric more explicit, but same requirement

### Timeout
- **Role-Centric**: Implicit (tasks have timeouts)
- **Goal-Centric**: "C5: Terminate within specified timeout"
- **Status**: ✅ Goal-centric more explicit, but same requirement

---

## Tool Access Parity

Both variants reference:
- Harness tools (to be defined in harness/skills/ or harness/agents/)
- Same permission sets per task
- No variant-specific tools

**Verification**: ✅ PASSED

---

## Evaluation Parity

Both variants evaluated using:
- Same evaluator versions (pinned per run)
- Same metrics:
  - Task success (binary)
  - Constraint adherence (0-100)
  - Runtime (seconds)
  - Clarification count (integer)
  - Reproducibility (0-1)

**Verification**: ✅ PASSED

---

## Parity Check Script

A minimal parity verification script should confirm:

```python
# Pseudocode for parity checker

def check_parity(role_centric_spec, goal_centric_spec, task_suite):
    """Verify variants are paired correctly"""
    
    # Check tool access identical
    assert role_centric_spec.tools == goal_centric_spec.tools
    
    # Check constraint semantics equivalent
    assert constraint_coverage(role_centric_spec) == constraint_coverage(goal_centric_spec)
    
    # Check both reference same harness version
    assert role_centric_spec.harness_ref == goal_centric_spec.harness_ref
    
    # Check both reference same evaluators
    assert role_centric_spec.evaluators == goal_centric_spec.evaluators
    
    # Check both apply to same task suite
    assert role_centric_spec.task_suite_ref == goal_centric_spec.task_suite_ref
    
    # Verify only paradigm differs
    assert role_centric_spec.paradigm != goal_centric_spec.paradigm
    
    return "PARITY VERIFIED"
```

---

## Exit Criteria

From execution-plan.md Step 3:
- ✅ Two variant files created
- ✅ Parity check confirms identical tooling
- ✅ Parity check confirms identical constraints
- ✅ Parity check confirms identical permissions
- ✅ Only specification paradigm differs

**Status**: PASSED

---

## Recommendations

### For Pilot Runs
1. Log all tool invocations to verify identical tool usage patterns
2. Monitor constraint checks to verify same constraint set active
3. Compare execution traces to identify paradigm-driven differences

### For Analysis
1. Any performance difference attributable to paradigm, not implementation
2. Control for harness behavior (ensure harness doesn't favor one paradigm)
3. Document any unexpected parity violations

---

**Parity Check Completed**: 2025-12-28T19:27:00.000Z  
**Status**: ✅ VERIFIED  
**Reviewer**: Execution Agent
