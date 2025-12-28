#!/usr/bin/env python3
"""
Runtime Evaluator

Calculates runtime metrics from execution log with timestamps.
"""

import json
from datetime import datetime
from typing import Dict, Any


def calculate_phase_durations(execution_log: Dict) -> Dict[str, float]:
    """Calculate time spent in each execution phase"""
    phases = {}
    events = execution_log.get('events', [])
    
    phase_start = {}
    for event in events:
        event_type = event.get('type')
        timestamp = event.get('timestamp')
        
        if event_type.endswith('_start'):
            phase = event_type.replace('_start', '')
            phase_start[phase] = datetime.fromisoformat(timestamp)
        elif event_type.endswith('_end'):
            phase = event_type.replace('_end', '')
            if phase in phase_start:
                start = phase_start[phase]
                end = datetime.fromisoformat(timestamp)
                phases[phase] = (end - start).total_seconds()
    
    return phases


def evaluate_runtime(execution_log: Dict) -> Dict[str, Any]:
    """
    Calculate runtime metrics from execution log
    
    Args:
        execution_log: Agent execution log with timestamps
    
    Returns:
        dict: Runtime metrics
    """
    start_time_str = execution_log.get('start_timestamp')
    end_time_str = execution_log.get('end_timestamp')
    
    if not start_time_str or not end_time_str:
        return {
            'error': 'Missing timestamps',
            'evaluator': 'runtime',
            'version': '1.0.0'
        }
    
    start_time = datetime.fromisoformat(start_time_str)
    end_time = datetime.fromisoformat(end_time_str)
    
    total_seconds = (end_time - start_time).total_seconds()
    timeout = execution_log.get('timeout_seconds', float('inf'))
    
    phases = calculate_phase_durations(execution_log)
    
    return {
        'total_seconds': total_seconds,
        'phases': phases,
        'timeout_seconds': timeout,
        'timeout_reached': total_seconds >= timeout,
        'evaluator': 'runtime',
        'version': '1.0.0'
    }


def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate runtime')
    parser.add_argument('--execution-log', required=True, help='Path to execution log JSON')
    parser.add_argument('--output', required=True, help='Path to write evaluation results')
    
    args = parser.parse_args()
    
    with open(args.execution_log) as f:
        execution_log = json.load(f)
    
    results = evaluate_runtime(execution_log)
    
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Runtime: {results.get('total_seconds', 'N/A')}s")
    return 0


if __name__ == '__main__':
    exit(main())
