#!/usr/bin/env python3
"""
Compute Aggregates

Computes aggregate statistics across all runs by variant.
"""

import pandas as pd
import numpy as np
import sys


def compute_aggregates(scorecard_index_path: str, output_path: str):
    """
    Compute aggregate statistics per variant
    
    Args:
        scorecard_index_path: Path to scorecard index CSV
        output_path: Path to write summary CSV
    """
    df = pd.read_csv(scorecard_index_path)
    
    # Group by variant
    summary = df.groupby('variant').agg({
        'task_success': ['mean', 'std', 'count'],
        'constraint_adherence': ['mean', 'std', 'min', 'max'],
        'runtime': ['mean', 'std', 'median'],
        'clarification_count': ['sum', 'mean', 'std'],
        'reproducibility': ['mean', 'std']
    })
    
    print("Variant Summary:")
    print(summary)
    
    summary.to_csv(output_path)
    print(f"\n✓ Summary written to {output_path}")
    
    # Also compute per-task breakdown
    task_summary = df.groupby(['task_id', 'variant']).agg({
        'task_success': 'mean',
        'constraint_adherence': 'mean',
        'runtime': 'mean',
        'clarification_count': 'mean'
    })
    
    task_output = output_path.replace('.csv', '_by_task.csv')
    task_summary.to_csv(task_output)
    print(f"✓ Task breakdown written to {task_output}")


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Compute aggregate statistics')
    parser.add_argument('--scorecard-index', required=True, help='Path to scorecard index CSV')
    parser.add_argument('--output', required=True, help='Path to write summary CSV')
    
    args = parser.parse_args()
    
    compute_aggregates(args.scorecard_index, args.output)
