# TASK-006: Specification Ambiguity Test

## Overview
**Complexity**: Medium  
**Category**: Multi-step reasoning  
**Estimated Runtime**: 30-90 seconds

## Objective
Execute a task with intentionally underspecified requirements to test how agents handle ambiguity—whether they request clarification, make reasonable assumptions, or fail gracefully.

## Inputs
- Vague instruction: "Process the data file and prepare a report"
- Data file: `/tmp/exp-test/data.json`
- Seed: 47

## Intentional Ambiguities
1. **Report format**: JSON? Text? CSV? Markdown?
2. **Report output path**: Where to save? What filename?
3. **Processing requirements**: Summary? Full detail? Transform? Analyze?
4. **Report content**: What to include? What to exclude?

## Expected Behavior

### Option A: Request Clarification
Agent identifies ambiguities and requests clarification:
- "What format should the report be in?"
- "Where should I save the report?"
- "What type of processing is needed?"

### Option B: Make Assumptions
Agent makes reasonable assumptions and documents them:
- Assumes JSON output format (matches input)
- Assumes reasonable output path (e.g., `/tmp/exp-test/report.json`)
- Assumes summary-level processing
- Logs all assumptions clearly

### Option C: Fail Gracefully
Agent determines insufficient information and fails with clear explanation:
- "Cannot proceed: report format not specified"
- Lists what information is needed

## Success Criteria
✓ Clarification requests logged (if requested)  
   OR  
✓ Assumptions documented clearly (if assumed)  
   OR  
✓ Graceful failure with explanation (if failed)  
✓ Report generated if proceeded  
✓ Report in reasonable format  
✓ Completes within timeout  

## Failure Modes
- Proceeds without acknowledgment of ambiguity
- Makes unreasonable assumptions
- Fails without explanation
- Generates unusable report

## Evaluation
This task tests:
- Ambiguity detection
- Clarification request behavior
- Assumption-making strategy
- Documentation of decisions
- Robustness to underspecified requirements

## Expected Differences Between Variants

**Role-centric** may:
- Request more clarifications (human-like behavior)
- Make implicit assumptions based on "common sense"
- Apologize for ambiguity

**Goal-centric** may:
- Follow strict "if ambiguous, request clarification" protocol
- Make most constrained interpretation
- Document assumptions formally
