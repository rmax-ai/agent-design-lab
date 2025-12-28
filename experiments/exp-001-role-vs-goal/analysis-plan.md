# Analysis Plan - exp-001-role-vs-goal

**Version**: 1.0  
**Date**: 2025-12-28  
**Status**: Design complete, execution pending run completion

---

## Overview

Aggregate and analyze results from ≥10 paired runs per task, following pre-registered analysis plan from research.md.

**Prerequisites**: Full runs completed (Step 7), all violations resolved or documented (Step 8).

---

## Data Aggregation (Step 9)

### Phase 1: Collect Scorecards

**1.1 Extract All Scorecards**

```bash
# Collect all scorecard files
find experiments/exp-001-role-vs-goal/runs/ \
  -name "scorecard.json" \
  -exec cp {} analysis/scorecards/ \;

# Generate scorecard index
./harness/workflows/synthesize --collect-scorecards \
  --experiment exp-001-role-vs-goal \
  --output analysis/scorecard-index.csv
```

**Expected Output**: `scorecard-index.csv`
```csv
run_id,variant,task_id,task_success,constraint_adherence,runtime,clarification_count,reproducibility
run-001a,role-centric,TASK-001,1,100.0,15.2,0,0.95
run-001b,goal-centric,TASK-001,1,100.0,14.8,0,0.95
...
```

### Phase 2: Validate Completeness

**2.1 Check Sample Size**

```python
# verify_sample_size.py

import pandas as pd

df = pd.read_csv('analysis/scorecard-index.csv')

# Check paired runs per task
for task in df['task_id'].unique():
    task_df = df[df['task_id'] == task]
    role_count = len(task_df[task_df['variant'] == 'role-centric'])
    goal_count = len(task_df[task_df['variant'] == 'goal-centric'])
    
    print(f"{task}: role={role_count}, goal={goal_count}")
    
    if role_count < 10 or goal_count < 10:
        print(f"  WARNING: Insufficient samples (min 10 required)")
    
    if role_count != goal_count:
        print(f"  WARNING: Unbalanced pairs")
```

**2.2 Check Data Quality**

- All metrics present (no nulls)
- Values in expected ranges
- Paired runs properly matched

### Phase 3: Compute Aggregate Statistics

**3.1 Per-Variant Aggregates**

```python
# compute_aggregates.py

import pandas as pd
import numpy as np

df = pd.read_csv('analysis/scorecard-index.csv')

# Group by variant
summary = df.groupby('variant').agg({
    'task_success': ['mean', 'std', 'count'],
    'constraint_adherence': ['mean', 'std', 'min', 'max'],
    'runtime': ['mean', 'std', 'median'],
    'clarification_count': ['sum', 'mean', 'std'],
    'reproducibility': ['mean', 'std']
})

print(summary)
summary.to_csv('analysis/variant-summary.csv')
```

**3.2 Per-Task Aggregates**

```python
# Compute stats per task
task_summary = df.groupby(['task_id', 'variant']).agg({
    'task_success': 'mean',
    'constraint_adherence': 'mean',
    'runtime': 'mean',
    'clarification_count': 'mean'
})

task_summary.to_csv('analysis/task-variant-summary.csv')
```

---

## Statistical Analysis (Step 9)

### Phase 4: Pre-Registered Tests

**4.1 Primary Hypothesis Test (H1): Task Success Rate**

```python
# test_h1_task_success.py

import pandas as pd
from scipy import stats

df = pd.read_csv('analysis/scorecard-index.csv')

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

# Effect size (Cohen's d)
diff = goal_success - role_success
cohens_d = diff.mean() / diff.std()

# Confidence interval
ci = stats.t.interval(
    confidence=0.95,
    df=len(diff)-1,
    loc=diff.mean(),
    scale=stats.sem(diff)
)

print(f"H1 Test Results:")
print(f"  t-statistic: {t_stat:.4f}")
print(f"  p-value: {p_value:.4f}")
print(f"  Cohen's d: {cohens_d:.4f}")
print(f"  95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print(f"  Result: SIGNIFICANT (p < {alpha})")
    if cohens_d > 0:
        print(f"  Direction: Goal-centric > Role-centric")
    else:
        print(f"  Direction: Role-centric > Goal-centric")
else:
    print(f"  Result: NOT SIGNIFICANT (p >= {alpha})")
```

**4.2 Secondary Hypothesis Tests**

- **H2 (Constraint Adherence)**: Paired t-test or Wilcoxon signed-rank
- **H3 (Reproducibility)**: Paired t-test
- **H4 (Clarification Count)**: Paired t-test or Wilcoxon
- **H5 (Runtime)**: Paired t-test (log-transformed if needed)

**4.3 Multiple Comparison Correction**

```python
# bonferroni_correction.py

from statsmodels.stats.multitest import multipletests

p_values = [p_h1, p_h2, p_h3, p_h4, p_h5]
alpha = 0.05

rejected, p_corrected, _, _ = multipletests(
    p_values,
    alpha=alpha,
    method='bonferroni'
)

for i, (hyp, p, p_cor, rej) in enumerate(zip(
    ['H1', 'H2', 'H3', 'H4', 'H5'],
    p_values,
    p_corrected,
    rejected
), 1):
    print(f"{hyp}: p={p:.4f}, p_corrected={p_cor:.4f}, "
          f"significant={rej}")
```

### Phase 5: Effect Size Estimation

```python
# effect_sizes.py

def cohens_d(x1, x2):
    """Cohen's d for paired samples"""
    diff = x1 - x2
    return diff.mean() / diff.std()

# Compute effect sizes for all metrics
effect_sizes = {
    'task_success': cohens_d(goal_success, role_success),
    'constraint_adherence': cohens_d(goal_constraint, role_constraint),
    'runtime': cohens_d(goal_runtime, role_runtime),
    'clarification_count': cohens_d(goal_clarif, role_clarif),
    'reproducibility': cohens_d(goal_repro, role_repro)
}

# Interpret
for metric, d in effect_sizes.items():
    magnitude = (
        "large" if abs(d) >= 0.8 else
        "medium" if abs(d) >= 0.5 else
        "small" if abs(d) >= 0.2 else
        "negligible"
    )
    print(f"{metric}: d={d:.4f} ({magnitude})")
```

### Phase 6: Power Analysis

```python
# power_analysis.py

from statsmodels.stats.power import TTestPower

power_analysis = TTestPower()

# Post-hoc power calculation
observed_effect = cohens_d(goal_success, role_success)
n_pairs = len(paired_data)
alpha = 0.05

power = power_analysis.solve_power(
    effect_size=observed_effect,
    nobs=n_pairs,
    alpha=alpha,
    alternative='two-sided'
)

print(f"Statistical Power: {power:.4f}")
print(f"Sample Size: {n_pairs}")
print(f"Effect Size: {observed_effect:.4f}")

if power < 0.80:
    print("WARNING: Underpowered (< 0.80)")
```

---

## Visualization (Step 9)

### Figure 1: Success Rate Comparison

```python
# plot_success_rates.py

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart: Mean success rate by variant
fig, ax = plt.subplots(figsize=(8, 6))

summary_data = df.groupby('variant')['task_success'].agg(['mean', 'std'])

summary_data['mean'].plot(
    kind='bar',
    yerr=summary_data['std'],
    ax=ax,
    color=['#FF6B6B', '#4ECDC4']
)

ax.set_ylabel('Task Success Rate')
ax.set_xlabel('Variant')
ax.set_title('Task Success Rate by Agent Specification Paradigm')
ax.set_ylim([0, 1])
ax.legend(['Mean ± SD'])

plt.tight_layout()
plt.savefig('report/figures/fig1_success_rates.png', dpi=300)
```

### Figure 2: Paired Comparison Scatter

```python
# Scatter plot: Paired runs
fig, ax = plt.subplots(figsize=(8, 8))

ax.scatter(
    role_success,
    goal_success,
    alpha=0.6,
    s=100
)

# Add diagonal line (equality)
ax.plot([0, 1], [0, 1], 'k--', alpha=0.3, label='Equal performance')

ax.set_xlabel('Role-Centric Success Rate')
ax.set_ylabel('Goal-Centric Success Rate')
ax.set_title('Paired Comparison: Task Success Rates')
ax.legend()

plt.tight_layout()
plt.savefig('report/figures/fig2_paired_scatter.png', dpi=300)
```

### Figure 3: Distribution Plots

```python
# Distribution comparison
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

metrics = ['task_success', 'constraint_adherence', 
           'runtime', 'clarification_count']

for ax, metric in zip(axes.flat, metrics):
    for variant in ['role-centric', 'goal-centric']:
        data = df[df['variant'] == variant][metric]
        ax.hist(data, alpha=0.5, label=variant, bins=20)
    
    ax.set_xlabel(metric.replace('_', ' ').title())
    ax.set_ylabel('Frequency')
    ax.legend()

plt.tight_layout()
plt.savefig('report/figures/fig3_distributions.png', dpi=300)
```

### Figure 4: Reproducibility Heatmap

```python
# Reproducibility scores by task and variant
repro_matrix = df.pivot_table(
    index='task_id',
    columns='variant',
    values='reproducibility',
    aggfunc='mean'
)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(repro_matrix, annot=True, fmt='.3f', cmap='RdYlGn',
            vmin=0.7, vmax=1.0, ax=ax)
ax.set_title('Mean Reproducibility Score by Task and Variant')

plt.tight_layout()
plt.savefig('report/figures/fig4_reproducibility.png', dpi=300)
```

---

## Analysis Outputs

### Deliverables

1. **analysis/scorecard-index.csv** - Master data file
2. **analysis/variant-summary.csv** - Aggregate statistics
3. **analysis/task-variant-summary.csv** - Per-task breakdown
4. **analysis/statistical-tests.json** - Test results
5. **analysis/effect-sizes.json** - Effect size estimates
6. **report/figures/** - All visualizations
7. **report/analysis-notebook.ipynb** - Reproducible analysis

---

## Quality Checks

### Assumption Verification

**Normality**: Shapiro-Wilk test on differences
```python
from scipy.stats import shapiro
stat, p = shapiro(diff)
print(f"Normality test: W={stat:.4f}, p={p:.4f}")
```

**Outliers**: Identify extreme values
```python
# Z-score method
z_scores = np.abs(stats.zscore(df['runtime']))
outliers = df[z_scores > 3]
print(f"Outliers: {len(outliers)}")
```

### Sensitivity Analysis

- Re-run tests excluding outliers
- Re-run with different alpha levels
- Check robustness to missing data

---

## Exit Criteria

From execution-plan.md Step 9:
- ✅ Scorecards aggregated
- ✅ Effect sizes computed
- ✅ Confidence intervals calculated
- ✅ Pre-registered statistical tests performed
- ✅ Analysis reproducible and passes QC

**Ready for**: Step 10 (Produce Comparative Report)

---

**Status**: Plan ready, execution pending run completion  
**Version**: 1.0  
**Created**: 2025-12-28T19:33:00.000Z
