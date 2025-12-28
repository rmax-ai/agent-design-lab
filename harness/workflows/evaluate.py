#!/usr/bin/env python3
"""
Evaluation Dispatcher

Dispatches all evaluator modules and generates scorecard.
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run_evaluator(evaluator_name: str, evaluator_config: dict, run_dir: Path) -> dict:
    """Run a single evaluator"""
    module = evaluator_config.get('module')
    
    if not module or not Path(module).exists():
        return {
            'error': f'Evaluator module not found: {module}',
            'evaluator': evaluator_name
        }
    
    # Prepare evaluator-specific arguments
    output_file = run_dir / f'{evaluator_name}_results.json'
    
    # Common arguments (simplified - actual implementation would be more complex)
    cmd = [
        'python3', module,
        '--execution-log', str(run_dir / 'agent.log'),
        '--output', str(output_file)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0 and output_file.exists():
            with open(output_file) as f:
                return json.load(f)
        else:
            return {
                'error': f'Evaluator failed: {result.stderr}',
                'evaluator': evaluator_name
            }
    except Exception as e:
        return {
            'error': f'Evaluator exception: {str(e)}',
            'evaluator': evaluator_name
        }


def evaluate(manifest_path: str) -> dict:
    """
    Run all evaluators and generate scorecard
    
    Args:
        manifest_path: Path to run manifest
    
    Returns:
        dict: Complete scorecard
    """
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    run_id = manifest.get('run_id')
    run_dir = Path(manifest_path).parent
    
    # Get evaluator configurations
    evaluator_versions = manifest.get('pins', {}).get('evaluator_versions', {})
    
    # Run each evaluator
    metrics = {}
    for evaluator_name, evaluator_config in evaluator_versions.items():
        print(f'Running evaluator: {evaluator_name}...')
        result = run_evaluator(evaluator_name, evaluator_config, run_dir)
        metrics[evaluator_name] = result
    
    # Generate scorecard
    scorecard = {
        'run_id': run_id,
        'variant': manifest.get('variant', {}).get('variant_id'),
        'task_id': manifest.get('task', {}).get('task_id'),
        'timestamp': datetime.now().isoformat(),
        'evaluator_versions': evaluator_versions,
        'metrics': metrics,
        'raw_outputs': str(run_dir / 'outputs'),
        'execution_log': str(run_dir / 'agent.log')
    }
    
    return scorecard


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate run and generate scorecard')
    parser.add_argument('--manifest', required=True, help='Path to manifest JSON')
    
    args = parser.parse_args()
    
    print(f'Evaluating run: {args.manifest}')
    
    try:
        scorecard = evaluate(args.manifest)
        
        # Write scorecard
        manifest_dir = Path(args.manifest).parent
        scorecard_path = manifest_dir / 'scorecard.json'
        
        with open(scorecard_path, 'w') as f:
            json.dump(scorecard, f, indent=2)
        
        print(f'✓ Scorecard generated: {scorecard_path}')
        return 0
    
    except Exception as e:
        print(f'✗ Evaluation failed: {e}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
