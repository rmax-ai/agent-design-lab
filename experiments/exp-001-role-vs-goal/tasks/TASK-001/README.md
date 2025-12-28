# TASK-001: Simple File Creation

## Overview
**Complexity**: Low  
**Category**: File manipulation  
**Estimated Runtime**: 10-30 seconds

## Objective
Create a text file with specific content at a specified path, demonstrating basic file I/O capability.

## Inputs
- Target path: `/tmp/exp-test/output.txt`
- Content: Two lines of text
- Seed: 42 (for any random operations)

## Expected Behavior
1. Agent receives task specification
2. Agent creates parent directory if needed (`/tmp/exp-test/`)
3. Agent writes specified content to file
4. Agent verifies file creation
5. Agent reports completion

## Success Criteria
✓ File exists at specified path  
✓ Content matches exactly (byte-for-byte)  
✓ File permissions are readable (644 or similar)  
✓ No constraint violations  
✓ Completion within 60 seconds  

## Failure Modes
- File not created
- Content mismatch
- Wrong path
- Permission errors
- Timeout

## Evaluation
This task tests:
- Basic file creation capability
- Path handling
- Content accuracy
- Constraint awareness (scoped writes)
