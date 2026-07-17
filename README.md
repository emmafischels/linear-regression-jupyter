

## ASSIGNMENT 3##

Altering this README.md to commit to the new branch in GitHub!

## Project Overview 
The purpose of assignment 3 was to furhter add diagnostic checks and clearer plots, as well as praciing the version-control workflow. 

## Changes to Assignment 2 linear-regression-jupyter plots and scripts 
- MSE was included in both my printed outputs and plot annotations
- Plots were saved to PNG files in the script version

## Pushing new changes to GitHub workflow
1. The repository was cloned to download all files and full version history to my computer
2. Changes to the scripts were added and then commited
3. A new branch (eaf/assignment3) was created and checked out
4. Once changes were committed locally, they were pushed to GitHub
5. Once the pull request was approved, it was merged into main to incorporate the new work into the main codebase
6. A tag was added for the merge in order to mark the final version for submission 

## URLs to submit for Assignment 3 ##
URL: 
1. Original main-branch commit URL before merging: https://github.com/emmafischels/linear-regression-jupyter/commit/63c3cb63e4bec6a128b6ecc25c306fa5dfd0c86b
2. eaf/assignment3 branch URL: https://github.com/emmafischels/linear-regression-jupyter/tree/eaf/assignment3
3. Tagged main-branch URL after the merge: https://github.com/emmafischels/linear-regression-jupyter/releases/tag/v1.0



## Project Overview

This project explores and compares the implementation of a simple linear regression analysis in **Python** and **R**. The goal of the assignment was to model the relationship between two variables, **Years of Experience** and **Salary**, using the provided `regression_data.csv` dataset.

The project demonstrates how the same statistical analysis can be performed in two different programming languages and compares the workflow for data loading, visualization, model fitting, evaluation, and automation through command-line scripts.

The analysis includes:
- Importing and inspecting a CSV dataset
- Visualizing relationships between variables
- Building linear regression models
- Plotting regression lines over observed data
- Evaluating model performance
- Exporting Jupyter Notebooks for sharing
- Converting analyses into reusable command-line scripts

---
The dataset contains two variables:

- **YearsExperience**: The number of years of professional experience

- **Salary**: The corresponding salary value

The objective is to predict salary based on years of experience using a linear regression model.

---

## Methods

Linear regression was performed using both Python and R to compare how each language approaches the same data analysis task.

### Data Analysis Workflow

For both languages, the workflow included:
1. Loading the dataset
2. Examining the data structure
3. Creating a scatter plot to visualize the relationship between experience and salary
4. Fitting a linear regression model
5. Generating predicted values
6. Overlaying the regression line on the original data
7. Evaluating model performance

---

## Tools and Libraries Used

### Python
Python was used for data analysis, visualization, and machine learning.
Libraries:
- **pandas** — data loading and manipulation
- **matplotlib** — data visualization
- **scikit-learn** — linear regression modeling

### R
R was used for statistical modeling and visualization.
Packages:
- **Base R** — data processing and linear modeling
- **ggplot2** — visualization and regression plots

### Computing Environment

The project was completed using:
- JupyterLab
- OSC OnDemand computing environment
- Conda environment (`7030_class_1`)

---

## Model Evaluation

The regression models were evaluated to determine how well Years of Experience predicts Salary.
Evaluation methods included:
- **R-squared (R²)** value in Python using the `LinearRegression.score()` function
- **Model summary statistics** in R using the `summary()` function
The results demonstrate the strength of the linear relationship between years of experience and salary.

---

## Command-Line Automation

The notebook analyses were converted into standalone scripts that allow the regression analysis to be performed directly from the terminal.

The scripts accept:
1. The input CSV filename
2. The independent variable (x-axis column)
3. The dependent variable (y-axis column)
