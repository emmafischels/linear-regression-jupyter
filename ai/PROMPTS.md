# AI Assignment Prompts Log

This file records the prompts used for each phase of the Assignment 3 AI workflow.

---

## Prompt 1 — Assignment 2 Baseline (Original AI Setup)

**Purpose:** Create the initial AI folder with Python and R notebooks, environment files, and CLI scripts.

```
Create and compare linear regression models in Python and R using Jupyter notebooks.
Using the regression_data.csv in the Assignment2/ai folder, create two jupyter notebooks
(one Python kernel, one R kernel). Each notebook should: read the dataset, create a scatter
plot, fit a linear model, overlay the regression line, and evaluate the model. Export HTML
versions. Generate environment.yml, requirements.txt, and setup_env.sh. Create CLI scripts
linear_regression_python.py and linear_regression_r.R accepting <filename> <x_column> <y_column>
and saving plot images.
```

---

## Prompt 2 — Assignment 3 AI Enhancement

**Purpose:** Branch from main, enhance regression analysis with diagnostics and annotated plots, and demonstrate GitHub workflow.

```
In a new AI folder, clone the Assignment 2 repo, create an assignment3AI branch, enhance
the regression analysis with detailed diagnostics and annotated plots, and demonstrate GitHub
workflow proficiency through pull requests and tagging. Deliverables: (1) original main-branch
commit URL before merging assignment 3, (2) assignment3 branch URL, (3) tagged main-branch
URL after the merge. Review the assignment3 PR diff and save as ai/CODE_REVIEW.md. Generate
a fresh README from code as ai/README_AI.md without overriding the manual README. Log prompts
in ai/PROMPTS.md. Do not delete or override existing files.
```

**Clarification from user:**

```
Create a branch from the main branch in assignment2 (linear_regression_jupyter on GitHub).
Add an additional AI branch and do your work there. Proceed with new PR, merge, and tag from
assignment3AI rather than reusing the earlier eaf/assignment3 merge.
```

---

## Prompt 3 — Documentation and Code Review

**Purpose:** Review the assignment3AI PR diff, generate README_AI.md from the enhanced code, and complete the prompts log.

```
Review your assignment3AI PR diff. Save the review as ai/CODE_REVIEW.md in the repo.
Generate a fresh README from my code. Save it as ai/README_AI.md but do not override my
manual README. For the prompts log, use ai/PROMPTS.md with the prompts used for each of
the three workflow phases (baseline setup, AI enhancement, documentation/review).
```
