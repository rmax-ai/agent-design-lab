#!/usr/bin/env python3
"""
Manifest Validator

Validates run manifests meet all requirements before execution.
"""

import json
import sys
from pathlib import Path


def validate_manifest(manifest_path: str) -> dict:
    """
    Validate run manifest before execution
    
    Returns:
        dict: Validation results with valid status, errors, and warnings
    """
    errors = []
    warnings = []
    
    manifest_file = Path(manifest_path)
    if not manifest_file.exists():
        return {
            'valid': False,
            'errors': [f'Manifest file not found: {manifest_path}'],
            'warnings': []
        }
    
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        return {
            'valid': False,
            'errors': [f'Invalid JSON: {e}'],
            'warnings': []
        }
    
    # Check schema version
    if manifest.get('manifest_version') != '1.0':
        errors.append('Invalid manifest version (expected 1.0)')
    
    # Check all pins present
    pins = manifest.get('pins', {})
    required_pins = [
        'harness_version',
        'evaluator_versions',
        'tool_permission_set'
    ]
    for pin in required_pins:
        if pin not in pins:
            errors.append(f'Missing pin: {pin}')
    
    # Check no floating versions
    evaluator_versions = pins.get('evaluator_versions', {})
    for evaluator, config in evaluator_versions.items():
        if not config.get('version'):
            errors.append(f'Evaluator {evaluator} has no version pin')
        if not config.get('hash'):
            warnings.append(f'Evaluator {evaluator} has no hash pin')
    
    # Check variant specification exists
    variant = manifest.get('variant', {})
    variant_spec = variant.get('specification_file')
    if variant_spec:
        if not Path(variant_spec).exists():
            errors.append(f'Variant specification not found: {variant_spec}')
    else:
        errors.append('No variant specification file specified')
    
    # Check task specification exists
    task = manifest.get('task', {})
    task_spec = task.get('specification_file')
    if task_spec:
        if not Path(task_spec).exists():
            errors.append(f'Task specification not found: {task_spec}')
    else:
        errors.append('No task specification file specified')
    
    # Check input snapshots
    inputs = manifest.get('inputs', {})
    input_path = inputs.get('snapshot_path')
    if input_path:
        if not Path(input_path).exists():
            warnings.append(f'Input snapshot path not found: {input_path}')
    
    valid = len(errors) == 0
    
    return {
        'valid': valid,
        'errors': errors,
        'warnings': warnings
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate run manifest')
    parser.add_argument('--manifest', required=True, help='Path to manifest JSON')
    
    args = parser.parse_args()
    
    result = validate_manifest(args.manifest)
    
    if result['valid']:
        print('✓ VALIDATION PASSED')
        if result['warnings']:
            print('\nWarnings:')
            for warning in result['warnings']:
                print(f'  ⚠ {warning}')
        return 0
    else:
        print('✗ VALIDATION FAILED')
        print('\nErrors:')
        for error in result['errors']:
            print(f'  ✗ {error}')
        if result['warnings']:
            print('\nWarnings:')
            for warning in result['warnings']:
                print(f'  ⚠ {warning}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
