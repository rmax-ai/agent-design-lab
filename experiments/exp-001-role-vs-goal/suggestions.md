# Suggestions for Improvement - exp-001-role-vs-goal

## Task Execution Improvements

### 1. Automation Opportunities
- Consider creating helper scripts for common operations (with awareness they should be general-purpose)
- Template generators for run manifests could reduce errors

### 2. Documentation
- execution-plan.md is clear and actionable
- Would benefit from links to related files (research.md, manifest.md)

### 3. Tracking Infrastructure
- Current approach: separate files for status, notes, suggestions, feedback
- Could benefit from timestamps on each entry
- Status file uses checkboxes for easy progress visualization

### 4. Workflow Clarity
- The 12-step plan is comprehensive
- Each step has clear deliverables and exit criteria
- Estimated effort timelines help with planning

## Future Considerations
- Consider adding a CHANGELOG.md for experiment-level changes
- Version control strategy for iterative improvements to tasks/variants
- Automated validation scripts for manifest/scorecard schemas

## Improvements Identified During Execution

### 5. Clear Separation of Planning vs Implementation
- **Observation**: Execution plan steps 1-5 are primarily planning/design
- **Observation**: Steps 6-12 require actual harness implementation
- **Suggestion**: Consider splitting execution plans into:
  - Phase A: Design & Specification (steps 1-5)
  - Phase B: Implementation & Validation (steps 6-8)
  - Phase C: Execution & Analysis (steps 9-12)
- **Benefit**: Clearer milestones, better resource planning

### 6. Harness as Separate Component
- **Observation**: Harness is shared infrastructure, not experiment-specific
- **Suggestion**: Harness development should be a separate initiative
- **Suggestion**: Each experiment references harness versions but doesn't build it
- **Benefit**: Reusable infrastructure, cleaner separation of concerns

### 7. Template Reusability
- **Observation**: Many artifacts created are templates/schemas
- **Suggestion**: Move common templates to project-level or harness-level
- **Examples**: run-manifest-template, evaluator-config patterns
- **Benefit**: Consistency across experiments, easier updates

### 8. Documentation Quality
- **Success**: Comprehensive documentation created for all components
- **Suggestion**: Consider adding diagrams (workflow flowcharts, architecture)
- **Suggestion**: Add "quick start" guide for running pilot
- **Benefit**: Easier onboarding for new contributors

### 9. Pilot-First Approach
- **Success**: Pilot plan created before full implementation
- **Benefit**: Validates design before committing to full runs
- **Suggestion**: Make pilot-first approach standard for all experiments
- **Suggestion**: Include pilot budget in experiment planning

### 10. Pre-Registration Rigor
- **Success**: Comprehensive pre-registration before any data collection
- **Benefit**: Prevents p-hacking, ensures scientific integrity
- **Suggestion**: Include pre-registration as mandatory step in all experiments
- **Suggestion**: Pre-registration review by independent party

