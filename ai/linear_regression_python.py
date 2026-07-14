import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
x = data[[x_col]].values
y = data[[y_col]].values.ravel()

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
residuals = y - y_pred

n = len(y)
p = 1
r_squared = model.score(x, y)
adj_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
intercept = float(np.atleast_1d(model.intercept_)[0])
slope = float(np.atleast_1d(model.coef_.ravel())[0])
rmse = np.sqrt(np.mean(residuals**2))

x_line_flat = np.linspace(x.min(), x.max(), 100)
x_line = x_line_flat.reshape(-1, 1)
y_line = model.predict(x_line).ravel()
residual_std = np.std(residuals, ddof=2)
t_crit = stats.t.ppf(0.975, n - p - 1)
x_mean = x.mean()
x_ss = np.sum((x - x_mean) ** 2)
ci_margin = t_crit * residual_std * np.sqrt(1 / n + (x_line_flat - x_mean) ** 2 / x_ss)
y_upper = y_line + ci_margin
y_lower = y_line - ci_margin

fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(data[x_col], data[y_col], color="red", alpha=0.8, label="Observed")
ax.plot(x_line_flat, y_line, color="blue", linewidth=2, label="Fitted line")
ax.fill_between(x_line_flat, y_lower, y_upper, color="blue", alpha=0.15, label="95% CI")
equation = f"{y_col} = {intercept:,.0f} + {slope:,.0f} * {x_col}"
annotation = (
    f"{equation}\n"
    f"R² = {r_squared:.4f}\n"
    f"Adj. R² = {adj_r_squared:.4f}\n"
    f"RMSE = {rmse:,.0f}"
)
ax.annotate(
    annotation,
    xy=(0.05, 0.95),
    xycoords="axes fraction",
    va="top",
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.85),
    fontsize=10,
)
ax.set_title(f"{y_col} vs {x_col} — Annotated Linear Regression")
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.legend(loc="lower right")
fig.tight_layout()
fig.savefig("linear_regression_python_output.png", dpi=150)
fig.savefig("regression_plot_python.png", dpi=150)
plt.close(fig)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].scatter(y_pred, residuals, color="steelblue", alpha=0.8)
axes[0, 0].axhline(0, color="gray", linestyle="--")
axes[0, 0].set_title("Residuals vs Fitted")
axes[0, 0].set_xlabel("Fitted values")
axes[0, 0].set_ylabel("Residuals")

stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title("Normal Q-Q Plot")

standardized_residuals = residuals / residual_std
axes[1, 0].scatter(y_pred, np.sqrt(np.abs(standardized_residuals)), color="darkorange", alpha=0.8)
axes[1, 0].set_title("Scale-Location")
axes[1, 0].set_xlabel("Fitted values")
axes[1, 0].set_ylabel("√|Standardized residuals|")

axes[1, 1].hist(residuals, bins=6, color="seagreen", edgecolor="white", alpha=0.85)
axes[1, 1].set_title("Residual Distribution")
axes[1, 1].set_xlabel("Residual")
axes[1, 1].set_ylabel("Count")

fig.suptitle("Regression Diagnostic Plots (Python)", fontsize=12)
fig.tight_layout()
fig.savefig("regression_diagnostics_python.png", dpi=150)
plt.close(fig)

leverage = (1 / n) + ((x - x.mean()) ** 2 / np.sum((x - x.mean()) ** 2)).ravel()
cooks_d = (residuals**2 / (p * residual_std**2)) * (leverage / (1 - leverage) ** 2)

print("=== Linear Regression Diagnostics (Python) ===")
print(f"Observations: {n}")
print(f"Intercept: {intercept:,.2f}")
print(f"Slope ({x_col}): {slope:,.2f}")
print(f"R-squared: {r_squared:.4f}")
print(f"Adjusted R-squared: {adj_r_squared:.4f}")
print(f"RMSE: {rmse:,.2f}")
print(f"Residual mean: {residuals.mean():,.2f}")
print(f"Residual std: {residual_std:,.2f}")
print(f"Max |residual|: {np.max(np.abs(residuals)):,.2f}")
print(f"Max Cook's distance: {cooks_d.max():.4f}")
print("Saved plot to linear_regression_python_output.png")
print("Saved annotated plot to regression_plot_python.png")
print("Saved diagnostics to regression_diagnostics_python.png")
