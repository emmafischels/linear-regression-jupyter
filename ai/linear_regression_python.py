import sys

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[x_col], data[y_col], color="red")
plt.plot(data[x_col], model.predict(data[[x_col]]), color="blue")
plt.title(f"{y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.close()

r_squared = model.score(data[[x_col]], data[[y_col]])
print(f"R-squared: {r_squared:.4f}")
print("Saved plot to linear_regression_python_output.png")
