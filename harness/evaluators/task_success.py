#!/usr/bin/env python3
"""
Task Success Evaluator

Evaluates whether task requirements were satisfied based on task specification,
agent outputs, and expected outputs.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, Any, List


def check_criterion(criterion: str, agent_outputs: Dict, expected_outputs: Dict) -> bool:
    """
    Check if a specific success criterion is met
    
    Args:
        criterion: Success criterion to check
        agent_outputs: Outputs produced by agent
        expected_outputs: Expected outputs from task spec
    
    Returns:
        bool: True if criterion met
    """
    # Implement criterion checks
    if criterion == "file_exists":
        path = expected_outputs.get("file_path")
        return Path(path).exists() if path else False
    
    elif criterion == "content_matches_exactly":
        path = expected_outputs.get("file_path")
        expected_hash = expected_outputs.get("content_sha256")
        if not path or not Path(path).exists():
            return False
        with open(path, 'rb') as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()
        return actual_hash == expected_hash
    
    elif criterion == "json_well_formed":
        output_path = agent_outputs.get("output_file")
        if not output_path or not Path(output_path).exists():
            return False
        try:
            with open(output_path) as f:
                json.load(f)
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False
    
    elif criterion == "no_constraint_violations":
        violations = agent_outputs.get("violations", [])
        return len(violations) == 0
    
    # Default: criterion not recognized
    return False


def generate_rationale(results: Dict[str, bool]) -> str:
    """Generate explanation for evaluation result"""
    passed = [k for k, v in results.items() if v]
    failed = [k for k, v in results.items() if not v]
    
    if not failed:
        return "All success criteria met"
    elif not passed:
        return f"All criteria failed: {', '.join(failed)}"
    else:
        return f"Partial success. Passed: {', '.join(passed)}. Failed: {', '.join(failed)}"


def evaluate_task_success(task_spec: Dict, agent_outputs: Dict, expected_outputs: Dict) -> Dict[str, Any]:
    """
    Evaluate whether task requirements were satisfied
    
    Args:
        task_spec: Task specification with success criteria
        agent_outputs: Agent outputs and metadata
        expected_outputs: Expected outputs from task
    
    Returns:
        dict: Evaluation results with success status, rationale, and details
    """
    criteria = task_spec.get('success_criteria', [])
    results = {}
    
    for criterion in criteria:
        results[criterion] = check_criterion(criterion, agent_outputs, expected_outputs)
    
    success = all(results.values())
    rationale = generate_rationale(results)
    
    return {
        'success': success,
        'rationale': rationale,
        'criteria_results': results,
        'evaluator': 'task_success',
        'version': '1.0.0'
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate task success')
    parser.add_argument('--task-spec', required=True, help='Path to task spec JSON')
    parser.add_argument('--agent-outputs', required=True, help='Path to agent outputs JSON')
    parser.add_argument('--expected-outputs', required=True, help='Path to expected outputs JSON')
    parser.add_argument('--output', required=True, help='Path to write evaluation results')
    
    args = parser.parse_args()
    
    with open(args.task_spec) as f:
        task_spec = json.load(f)
    with open(args.agent_outputs) as f:
        agent_outputs = json.load(f)
    with open(args.expected_outputs) as f:
        expected_outputs = json.load(f)
    
    results = evaluate_task_success(task_spec, agent_outputs, expected_outputs)
    
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Evaluation complete: {'PASS' if results['success'] else 'FAIL'}")
    return 0 if results['success'] else 1


if __name__ == '__main__':
    exit(main())
