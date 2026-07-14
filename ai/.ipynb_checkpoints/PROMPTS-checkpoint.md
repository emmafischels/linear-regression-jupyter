# Key Prompts Used (Assignment 2 — Linear Regression)

The prompts below drove the AI-generated work in `Assignment2/ai/`.

---

## 1. Environment setup (do this first)

> Generate an `environment.yml`, a `requirements.txt`, and a `setup_env.sh` that builds the environment. Do this before creating any notebooks or scripts.

---

## 2. Jupyter notebooks (Python + R)

> Create two Jupyter notebooks in `Assignment2/ai/` using `regression_data.csv` — one with the Python kernel, one with the R kernel.
>
> Each notebook should:
> - Start with a markdown cell: *"This notebook demonstrates a simple linear regression analysis using [Python/R] to model Salary based on Years of Experience."*
> - Read the dataset
> - Create a scatter plot
> - Fit a linear model
> - Overlay the regression line
> - Evaluate the model
>
> Save each notebook as both `.ipynb` and exported `.html`. All outputs go in `Assignment2/ai/`.

---

## 3. Command-line scripts

> Create `linear_regression_python.py` and `linear_regression_r.R` converted from the notebooks.
>
> Both scripts must:
> - Accept command-line arguments: `<filename> <x_column> <y_column>`
> - Generate and save a plot image (`linear_regression_python_output.png`, `linear_regression_r_output.png`)
> - Have those output images committed to the repo

---

## 4. Manual vs. AI comparison

> Tell me how my manual code in Assignment2 files differs from your version structurally (libraries chosen, function decomposition, CLI parsing, plot defaults). Which one is more readable? Which would another scientist understand faster? Did the AI introduce bugs? Did it skip steps? Did the CLI behave as expected?

---

## 5. Document the prompts

> Create a short `PROMPTS.md` file with the 3–5 most important prompts you used.
