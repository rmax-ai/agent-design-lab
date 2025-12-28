#!/usr/bin/env python3
"""
Bonferroni Correction

Applies Bonferroni correction for multiple hypothesis testing.
"""

from statsmodels.stats.multitest import multipletests
import json
import sys


def bonferroni_correction(p_values: list, alpha: float = 0.05, hypothesis_names: list = None):
    """
    Apply Bonferroni correction to p-values
    
    Args:
        p_values: List of uncorrected p-values
        alpha: Family-wise error rate
        hypothesis_names: Optional names for hypotheses
    
    Returns:
        dict: Corrected results
    """
    if hypothesis_names is None:
        hypothesis_names = [f'H{i+1}' for i in range(len(p_values))]
    
    rejected, p_corrected, _, _ = multipletests(
        p_values,
        alpha=alpha,
        method='bonferroni'
    )
    
    results = []
    for i, (hyp, p, p_cor, rej) in enumerate(zip(
        hypothesis_names,
        p_values,
        p_corrected,
        rejected
    )):
        results.append({
            'hypothesis': hyp,
            'p_value': float(p),
            'p_corrected': float(p_cor),
            'significant': bool(rej),
            'alpha': alpha
        })
        print(f"{hyp}: p={p:.4f}, p_corrected={p_cor:.4f}, significant={rej}")
    
    return {
        'method': 'bonferroni',
        'alpha': alpha,
        'results': results
    }


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Apply Bonferroni correction')
    parser.add_argument('--p-values', required=True, nargs='+', type=float, help='Uncorrected p-values')
    parser.add_argument('--hypothesis-names', nargs='+', help='Optional hypothesis names')
    parser.add_argument('--alpha', type=float, default=0.05, help='Family-wise error rate')
    parser.add_argument('--output', required=True, help='Path to write results JSON')
    
    args = parser.parse_args()
    
    results = bonferroni_correction(args.p_values, args.alpha, args.hypothesis_names)
    
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Results written to {args.output}")
