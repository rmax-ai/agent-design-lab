# TASK-004: Error Recovery

## Overview
**Complexity**: Medium  
**Category**: Error handling  
**Estimated Runtime**: 45-120 seconds

## Objective
Attempt an operation that will fail initially, detect the failure, and retry with a corrected approach, demonstrating error handling and recovery capabilities.

## Inputs
- Target path: `/tmp/exp-test/nonexistent/data.txt` (parent directory doesn't exist)
- Content: "Data to write"
- Fallback path: `/tmp/exp-test/data.txt`
- Seed: 45

## Expected Behavior
1. Agent attempts to write to target_file
2. Operation fails (directory doesn't exist)
3. Agent detects and logs the error
4. Agent takes recovery action:
   - Option A: Create parent directory and retry
   - Option B: Use fallback_path
5. File successfully created with content
6. Error and recovery documented in logs

## Success Criteria
✓ File created successfully (at either location)  
✓ Initial error logged explicitly  
✓ Recovery action taken and logged  
✓ Task completes within timeout (150 seconds)  

## Failure Modes
- No error detection (silent failure)
- Error logged but no recovery attempted
- Recovery attempted but incorrect approach
- Timeout due to infinite retry loop

## Evaluation
This task tests:
- Error detection capability
- Logging of failures
- Recovery strategy selection
- Adaptability when constraints encountered
