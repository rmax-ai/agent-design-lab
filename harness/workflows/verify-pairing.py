#!/usr/bin/env python3
"""
Verify Pairing

Verifies that paired runs have identical inputs and seeds.
"""

import json
import sys
from pathlib import Path


def verify_pairing(pair_id: str, run_manifests: list) -> dict:
    """
    Verify that paired runs are correctly configured
    
    Args:
        pair_id: Pair identifier
        run_manifests: List of manifest file paths
    
    Returns:
        dict: Verification results
    """
    errors = []
    warnings = []
    
    if len(run_manifests) != 2:
        errors.append(f'Expected 2 runs in pair, found {len(run_manifests)}')
        return {'valid': False, 'errors': errors, 'warnings': warnings}
    
    # Load manifests
    manifests = []
    for manifest_path in run_manifests:
        with open(manifest_path) as f:
            manifests.append(json.load(f))
    
    run1, run2 = manifests
    
    # Check same task
    task1 = run1.get('task', {}).get('task_id')
    task2 = run2.get('task', {}).get('task_id')
    if task1 != task2:
        errors.append(f'Task mismatch: {task1} != {task2}')
    
    # Check same seed
    seed1 = run1.get('task', {}).get('seed')
    seed2 = run2.get('task', {}).get('seed')
    if seed1 != seed2:
        errors.append(f'Seed mismatch: {seed1} != {seed2}')
    
    # Check same timeout
    timeout1 = run1.get('task', {}).get('timeout_seconds')
    timeout2 = run2.get('task', {}).get('timeout_seconds')
    if timeout1 != timeout2:
        errors.append(f'Timeout mismatch: {timeout1} != {timeout2}')
    
    # Check different variants
    variant1 = run1.get('variant', {}).get('variant_id')
    variant2 = run2.get('variant', {}).get('variant_id')
    if variant1 == variant2:
        errors.append(f'Same variant in pair: {variant1}')
    
    # Check input hash equality
    input_files1 = run1.get('inputs', {}).get('files', [])
    input_files2 = run2.get('inputs', {}).get('files', [])
    
    hashes1 = {f['path']: f['hash'] for f in input_files1}
    hashes2 = {f['path']: f['hash'] for f in input_files2}
    
    if hashes1 != hashes2:
        errors.append('Input file hashes do not match')
    
    # Check pair_id consistency
    pair1 = run1.get('pairing', {}).get('pair_id')
    pair2 = run2.get('pairing', {}).get('pair_id')
    if pair1 != pair_id or pair2 != pair_id:
        warnings.append(f'Pair ID mismatch in manifests')
    
    valid = len(errors) == 0
    
    return {
        'valid': valid,
        'errors': errors,
        'warnings': warnings,
        'pair_id': pair_id,
        'runs': [r.get('run_id') for r in manifests]
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify paired runs')
    parser.add_argument('--pair-id', required=True, help='Pair identifier')
    parser.add_argument('--manifests', required=True, nargs=2, help='Paths to two manifest JSONs')
    
    args = parser.parse_args()
    
    result = verify_pairing(args.pair_id, args.manifests)
    
    if result['valid']:
        print(f"✓ PAIRING VERIFIED: {result['pair_id']}")
        print(f"  Runs: {', '.join(result['runs'])}")
        if result['warnings']:
            print('\nWarnings:')
            for warning in result['warnings']:
                print(f'  ⚠ {warning}')
        return 0
    else:
        print(f"✗ PAIRING VERIFICATION FAILED: {result['pair_id']}")
        print('\nErrors:')
        for error in result['errors']:
            print(f'  ✗ {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
