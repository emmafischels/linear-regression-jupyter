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
