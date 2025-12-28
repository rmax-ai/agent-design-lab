#!/usr/bin/env python3
"""
Test H1: Task Success

Performs paired t-test for primary hypothesis (task success rate).
"""

import pandas as pd
import numpy as np
from scipy import stats
import json
import sys


def test_h1_task_success(scorecard_index_path: str, output_path: str):
    """
    Test H1: Goal-centric agents have higher task success rates
    
    Args:
        scorecard_index_path: Path to scorecard index CSV
        output_path: Path to write results JSON
    """
    df = pd.read_csv(scorecard_index_path)
    
    # Prepare paired data
    paired_data = df.pivot_table(
        index=['task_id', 'pair_id'],
        columns='variant',
        values='task_success'
    ).dropna()
    
    role_success = paired_data['role-centric']
    goal_success = paired_data['goal-centric']
    
    # Paired t-test
    t_stat, p_value = stats.ttest_rel(goal_success, role_success)
    
    # Effect size (Cohen's d for paired samples)
    diff = goal_success - role_success
    cohens_d = diff.mean() / diff.std()
    
    # Confidence interval
    ci = stats.t.interval(
        confidence=0.95,
        df=len(diff)-1,
        loc=diff.mean(),
        scale=stats.sem(diff)
    )
    
    # Interpretation
    alpha = 0.05
    significant = p_value < alpha
    direction = "Goal-centric > Role-centric" if cohens_d > 0 else "Role-centric > Goal-centric"
    
    results = {
        'hypothesis': 'H1',
        'description': 'Goal-centric agents have higher task success rates',
        't_statistic': float(t_stat),
        'p_value': float(p_value),
        'cohens_d': float(cohens_d),
        'confidence_interval_95': [float(ci[0]), float(ci[1])],
        'significant': significant,
        'alpha': alpha,
        'direction': direction if significant else 'No significant difference',
        'sample_size': len(diff),
        'mean_difference': float(diff.mean())
    }
    
    # Print results
    print("H1 Test Results:")
    print(f"  t-statistic: {t_stat:.4f}")
    print(f"  p-value: {p_value:.4f}")
    print(f"  Cohen's d: {cohens_d:.4f}")
    print(f"  95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
    print(f"  Result: {'SIGNIFICANT' if significant else 'NOT SIGNIFICANT'} (p {'<' if significant else '>='} {alpha})")
    if significant:
        print(f"  Direction: {direction}")
    
    # Write results
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Results written to {output_path}")
    
    return results


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Test H1: Task success rates')
    parser.add_argument('--scorecard-index', required=True, help='Path to scorecard index CSV')
    parser.add_argument('--output', required=True, help='Path to write results JSON')
    
    args = parser.parse_args()
    
    test_h1_task_success(args.scorecard_index, args.output)
