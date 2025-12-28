#!/usr/bin/env python3
"""
Clarification Counter

Counts and categorizes clarification requests in agent execution log.
"""

import json
import re
from typing import Dict, Any, List


def matches_clarification_pattern(log_entry: Dict, patterns: List[str]) -> bool:
    """Check if log entry matches clarification patterns"""
    message = log_entry.get('message', '').lower()
    return any(re.search(pattern, message, re.IGNORECASE) for pattern in patterns)


def categorize_request(log_entry: Dict) -> str:
    """Categorize clarification request"""
    message = log_entry.get('message', '').lower()
    
    if 'missing' in message or 'not provided' in message:
        return 'missing_information'
    elif 'ambiguous' in message or 'unclear' in message or 'multiple' in message:
        return 'ambiguous_specification'
    elif 'constraint' in message or 'permission' in message:
        return 'constraint_clarification'
    elif 'format' in message or 'output' in message:
        return 'output_format'
    else:
        return 'other'


def count_clarifications(execution_log: Dict) -> Dict[str, Any]:
    """
    Count and categorize clarification requests
    
    Args:
        execution_log: Agent execution log
    
    Returns:
        dict: Clarification counts and details
    """
    clarification_patterns = [
        r'(?i)ask.*clarification',
        r'(?i)need.*clarification',
        r'(?i)unclear',
        r'(?i)ambiguous',
        r'(?i)missing.*information',
        r'(?i)request.*clarification',
        r'(?i)what.*format',
        r'(?i)where.*save',
        r'(?i)which.*option'
    ]
    
    requests = []
    log_entries = execution_log.get('entries', [])
    
    for log_entry in log_entries:
        if matches_clarification_pattern(log_entry, clarification_patterns):
            requests.append({
                'timestamp': log_entry.get('timestamp'),
                'content': log_entry.get('message'),
                'category': categorize_request(log_entry)
            })
    
    # Count by category
    categories = {}
    for req in requests:
        cat = req['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    return {
        'total_count': len(requests),
        'requests': requests,
        'categories': categories,
        'evaluator': 'clarification_counter',
        'version': '1.0.0'
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Count clarification requests')
    parser.add_argument('--execution-log', required=True, help='Path to execution log JSON')
    parser.add_argument('--output', required=True, help='Path to write evaluation results')
    
    args = parser.parse_args()
    
    with open(args.execution_log) as f:
        execution_log = json.load(f)
    
    results = count_clarifications(execution_log)
    
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Clarification requests: {results['total_count']}")
    return 0


if __name__ == '__main__':
    exit(main())
