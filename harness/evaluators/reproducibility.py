#!/usr/bin/env python3
"""
Reproducibility Evaluator

Compares outputs across runs with identical inputs/seeds to assess reproducibility.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, Any, List


def compute_file_hash(filepath: Path) -> str:
    """Compute SHA256 hash of file"""
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def compare_outputs(reference_run: Dict, comparison_run: Dict) -> List[Dict]:
    """Compare outputs between two runs"""
    differences = []
    
    ref_outputs = reference_run.get('outputs', {})
    cmp_outputs = comparison_run.get('outputs', {})
    
    # Compare file hashes
    ref_files = ref_outputs.get('files', [])
    cmp_files = cmp_outputs.get('files', [])
    
    ref_paths = {f['path']: f['hash'] for f in ref_files}
    cmp_paths = {f['path']: f['hash'] for f in cmp_files}
    
    all_paths = set(ref_paths.keys()) | set(cmp_paths.keys())
    
    for path in all_paths:
        if path not in ref_paths:
            differences.append({
                'type': 'missing_in_reference',
                'path': path,
                'run_id': comparison_run.get('run_id')
            })
        elif path not in cmp_paths:
            differences.append({
                'type': 'missing_in_comparison',
                'path': path,
                'run_id': comparison_run.get('run_id')
            })
        elif ref_paths[path] != cmp_paths[path]:
            differences.append({
                'type': 'hash_mismatch',
                'path': path,
                'run_id': comparison_run.get('run_id'),
                'ref_hash': ref_paths[path],
                'cmp_hash': cmp_paths[path]
            })
    
    return differences


def evaluate_reproducibility(runs_with_same_seed: List[Dict]) -> Dict[str, Any]:
    """
    Compare outputs across runs with identical inputs/seeds
    
    Args:
        runs_with_same_seed: List of run manifests with same seed
    
    Returns:
        dict: Reproducibility score and differences
    """
    if len(runs_with_same_seed) < 2:
        return {
            'score': None,
            'reason': 'insufficient_runs',
            'evaluator': 'reproducibility',
            'version': '1.0.0'
        }
    
    reference_run = runs_with_same_seed[0]
    differences = []
    
    for run in runs_with_same_seed[1:]:
        run_differences = compare_outputs(reference_run, run)
        differences.extend(run_differences)
    
    total_comparisons = len(runs_with_same_seed) - 1
    runs_with_differences = len(set(d['run_id'] for d in differences))
    identical_runs = total_comparisons - runs_with_differences
    
    score = identical_runs / total_comparisons if total_comparisons > 0 else 0
    
    return {
        'score': score,
        'differences': differences,
        'identical_runs': identical_runs,
        'total_comparisons': total_comparisons,
        'evaluator': 'reproducibility',
        'version': '1.0.0'
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate reproducibility')
    parser.add_argument('--runs', required=True, nargs='+', help='Paths to run manifest JSONs')
    parser.add_argument('--output', required=True, help='Path to write evaluation results')
    
    args = parser.parse_args()
    
    runs = []
    for run_path in args.runs:
        with open(run_path) as f:
            runs.append(json.load(f))
    
    results = evaluate_reproducibility(runs)
    
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    score = results.get('score')
    if score is not None:
        print(f"Reproducibility score: {score:.2%}")
    else:
        print(f"Reproducibility: {results.get('reason')}")
    return 0


if __name__ == '__main__':
    exit(main())
