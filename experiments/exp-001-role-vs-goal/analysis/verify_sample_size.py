#!/usr/bin/env python3
"""
Verify Sample Size

Checks that sufficient paired runs exist for each task.
"""

import pandas as pd
import sys


def verify_sample_size(scorecard_index_path: str, min_samples: int = 10) -> dict:
    """
    Verify sufficient samples for statistical analysis
    
    Args:
        scorecard_index_path: Path to scorecard index CSV
        min_samples: Minimum required samples per variant per task
    
    Returns:
        dict: Verification results
    """
    df = pd.read_csv(scorecard_index_path)
    
    results = {
        'sufficient': True,
        'tasks': {},
        'warnings': []
    }
    
    # Check paired runs per task
    for task in df['task_id'].unique():
        task_df = df[df['task_id'] == task]
        role_count = len(task_df[task_df['variant'] == 'role-centric'])
        goal_count = len(task_df[task_df['variant'] == 'goal-centric'])
        
        results['tasks'][task] = {
            'role_centric': role_count,
            'goal_centric': goal_count
        }
        
        print(f"{task}: role={role_count}, goal={goal_count}")
        
        if role_count < min_samples or goal_count < min_samples:
            results['sufficient'] = False
            results['warnings'].append(
                f"{task}: Insufficient samples (min {min_samples} required)"
            )
        
        if role_count != goal_count:
            results['warnings'].append(
                f"{task}: Unbalanced pairs (role={role_count}, goal={goal_count})"
            )
    
    return results


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify sample size')
    parser.add_argument('--scorecard-index', required=True, help='Path to scorecard index CSV')
    parser.add_argument('--min-samples', type=int, default=10, help='Minimum samples per variant')
    
    args = parser.parse_args()
    
    results = verify_sample_size(args.scorecard_index, args.min_samples)
    
    if results['sufficient']:
        print('\n✓ Sample size verification PASSED')
        sys.exit(0)
    else:
        print('\n✗ Sample size verification FAILED')
        for warning in results['warnings']:
            print(f'  ⚠ {warning}')
        sys.exit(1)
