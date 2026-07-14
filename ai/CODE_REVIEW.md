# Code Review: assignment3AI → main

**Reviewer:** AI Agent (Cursor)  
**Branch reviewed:** `assignment3AI`  
**Base branch:** `main`  
**Pre-merge `main` commit:** `121db26` — [Merge pull request #1](https://github.com/emmafischels/linear-regression-jupyter/commit/121db26a07d052ca6b50f6f2d523f56e663974ff)  
**Review date:** July 14, 2026

---

## Summary

This pull request enhances the `ai/` folder with annotated regression visualizations, four-panel diagnostic plots, expanded CLI output, and supporting documentation (`README_AI.md`, `PROMPTS.md`). The changes are scoped entirely to `ai/` and do not modify the root `README.md` or manual assignment files.

**Verdict:** Approve with minor follow-up (R plot artifacts should be generated in a Conda environment with R before final submission).

---

## Files Changed (11 files, +1520 / −1078 lines)

| File | Change type | Assessment |
|------|-------------|------------|
| `ai/linear_regression_python.py` | Modified | Strong improvement |
| `ai/linear_regression_r.R` | Modified | Strong improvement |
| `ai/linear_regression_python.ipynb` | Modified | Good — adds diagnostic cells |
| `ai/linear_regression_r.ipynb` | Modified | Good — adds diagnostic cells |
| `ai/regression_plot_python.png` | New | Generated artifact — correct |
| `ai/regression_diagnostics_python.png` | New | Generated artifact — correct |
| `ai/linear_regression_python_output.png` | Modified | Updated annotated plot |
| `ai/README_AI.md` | New | Clear, accurate documentation |
| `ai/PROMPTS.md` | Modified | Structured three-phase prompt log |
| `ai/environment.yml` | Modified | Adds `scipy` dependency |
| `ai/requirements.txt` | Modified | Adds `scipy` dependency |

---

## Strengths

### 1. Annotated regression plots (Python & R)

Both scripts now produce publication-quality annotated figures with:

- Regression equation on-plot
- R², adjusted R², and RMSE
- 95% confidence band around the fitted line
- Consistent color scheme (red points, blue line)

This directly addresses the Assignment 3 requirement for **annotated plots**.

### 2. Diagnostic depth

The four-panel diagnostic figure covers standard linear-model checks:

- Residuals vs fitted (linearity / homoscedasticity)
- Normal Q-Q plot (normality of residuals)
- Scale-location plot (spread of standardized residuals)
- Residual histogram (distribution shape)

Printed metrics include residual mean, standard deviation, max absolute residual, and **Cook's distance** for influence detection.

### 3. Scope discipline

- No files deleted
- Root `README.md` untouched
- Changes confined to `ai/`
- `PROMPTS.md` reformatted (not removed) — original Assignment 2 prompt preserved under Prompt 1

### 4. Documentation

`README_AI.md` accurately describes project structure, setup, CLI usage, and expected outputs. It correctly references companion files (`PROMPTS.md`, `CODE_REVIEW.md`) without replacing the manual README.

---

## Issues and Recommendations

### Minor — R plot PNGs not committed in this environment

`regression_plot_r.png` and `regression_diagnostics_r.png` are referenced in `README_AI.md` but were not generated because R is unavailable on the review machine. The R script logic mirrors the Python enhancements and should be run in the Conda environment:

```bash
conda activate 7030_class_1
cd ai/
Rscript linear_regression_r.R regression_data.csv YearsExperience Salary
```

**Recommendation:** Generate and commit R PNG outputs before final grading.

### Minor — Notebook JSON churn

The `.ipynb` files show large line-count deltas due to notebook serialization changes in addition to new cells. Functionally correct, but future edits could use `nbformat` with minimal metadata changes to reduce diff noise.

### Minor — `scipy` added as new dependency

Appropriate for `stats.probplot` and distribution functions. Documented in both `environment.yml` and `requirements.txt`. No conflict observed.

### Suggestion — HTML export

Existing `.html` notebook exports predate the diagnostic cells. Re-run `jupyter nbconvert` after executing notebooks to refresh HTML artifacts.

---

## Code Quality Notes

### `linear_regression_python.py`

- Correct handling of scalar vs array `intercept_` / `coef_` via `np.atleast_1d`
- Confidence interval calculation uses proper Student-t critical value with `n - p - 1` degrees of freedom
- Cook's distance computed manually without adding `statsmodels` — keeps dependencies lean
- Saves both legacy (`linear_regression_python_output.png`) and new (`regression_plot_python.png`) filenames for backward compatibility

### `linear_regression_r.R`

- Uses `predict(..., se.fit = TRUE)` for confidence ribbons — idiomatic R
- Diagnostic panel uses base R graphics (no extra packages beyond ggplot2)
- `cooks.distance(model)` leverages built-in R influence metrics

---

## Testing Performed

| Test | Result |
|------|--------|
| `python3 linear_regression_python.py regression_data.csv YearsExperience Salary` | Pass — plots and diagnostics generated |
| R script execution | Skipped — R not installed on review host |
| Root README unchanged | Pass |
| Manual files at repo root unchanged | Pass |

**Python output verified:**

- R² = 0.7852 (matches prior baseline)
- Adjusted R² = 0.7583
- Max Cook's distance = 0.7971

---

## Security / Data Review

- No credentials or secrets added
- No changes to `.gitignore`
- CSV data unchanged
- CLI scripts validate argument count before processing

---

## Approval

**Approved for merge** with the note that R-generated PNG files should be produced and committed when an R runtime is available.

Post-merge action: tag `main` with `v1.1-assignment3-ai` to mark the AI enhancement release.
