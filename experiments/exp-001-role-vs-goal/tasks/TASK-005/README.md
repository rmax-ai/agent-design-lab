# TASK-005: Tool Composition

## Overview
**Complexity**: High  
**Category**: Tool composition  
**Estimated Runtime**: 60-180 seconds

## Objective
Chain multiple operations (file search, read, parse, filter, transform, write) to accomplish a complex data processing task, demonstrating tool composition and workflow orchestration.

## Setup
Pre-populated CSV files in `/tmp/exp-test/data/`:
- records1.csv (100 rows with "status" column)
- records2.csv (150 rows with "status" column)
- records3.csv (75 rows with "status" column)

## Inputs
- Data directory: `/tmp/exp-test/data/`
- Search pattern: `*.csv`
- Filter column: "status"
- Filter value: "active"
- Output file: `/tmp/exp-test/filtered_results.json`
- Seed: 46

## Expected Behavior
1. Search for all CSV files in data directory
2. Read and parse each CSV file
3. Filter rows where status = "active"
4. Aggregate filtered results
5. Generate JSON output with:
   - Total rows scanned
   - Filtered row count
   - Source file list
   - Filter criteria used
   - Filtered results array

## Success Criteria
✓ All CSV files found and processed  
✓ Filtering logic correct (status = "active")  
✓ JSON output well-formed and valid  
✓ Result counts accurate  
✓ Efficient tool invocation (no redundant operations)  
✓ Completes within timeout (300 seconds)  

## Failure Modes
- Missing files (incomplete search)
- Parsing errors (CSV format issues)
- Incorrect filtering (wrong column or value)
- Malformed JSON output
- Inefficient approach (redundant reads, excessive operations)
- Timeout due to poor orchestration

## Evaluation
This task tests:
- Multi-step workflow orchestration
- File discovery and iteration
- Data parsing and transformation
- Filtering logic implementation
- Output formatting
- Efficiency of tool composition
