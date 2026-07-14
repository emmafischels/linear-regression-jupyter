args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

fitted_vals <- fitted(model)
residuals <- residuals(model)
r_squared <- summary(model)$r.squared
adj_r_squared <- summary(model)$adj.r.squared
coefs <- coef(model)
intercept <- coefs[1]
slope <- coefs[2]
rmse <- sqrt(mean(residuals^2))

library(ggplot2)

pred_grid <- data.frame(x_seq = seq(min(data[[x_col]]), max(data[[x_col]]), length.out = 100))
names(pred_grid)[1] <- x_col
pred_grid$fit <- predict(model, newdata = pred_grid)
pred_grid$se <- predict(model, newdata = pred_grid, se.fit = TRUE)$se.fit
pred_grid$lower <- pred_grid$fit - qt(0.975, df = model$df.residual) * pred_grid$se
pred_grid$upper <- pred_grid$fit + qt(0.975, df = model$df.residual) * pred_grid$se

equation <- sprintf("%s = %.0f + %.0f * %s", y_col, intercept, slope, x_col)
annotation <- sprintf(
  "%s\nR² = %.4f\nAdj. R² = %.4f\nRMSE = %.0f",
  equation, r_squared, adj_r_squared, rmse
)

annotated_plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red", alpha = 0.8) +
  geom_ribbon(
    data = pred_grid,
    aes_string(x = x_col, ymin = "lower", ymax = "upper"),
    inherit.aes = FALSE,
    fill = "blue",
    alpha = 0.15
  ) +
  geom_line(data = pred_grid, aes_string(x = x_col, y = "fit"), color = "blue", linewidth = 1) +
  annotate(
    "label",
    x = min(data[[x_col]]),
    y = max(data[[y_col]]),
    label = annotation,
    hjust = 0,
    vjust = 1,
    fill = "wheat",
    alpha = 0.85,
    size = 3.5
  ) +
  ggtitle(paste(y_col, "vs", x_col, "— Annotated Linear Regression")) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", annotated_plot, width = 9, height = 6, dpi = 150)
ggsave("regression_plot_r.png", annotated_plot, width = 9, height = 6, dpi = 150)

png("regression_diagnostics_r.png", width = 1000, height = 800)
par(mfrow = c(2, 2))
plot(fitted_vals, residuals, main = "Residuals vs Fitted", xlab = "Fitted values", ylab = "Residuals", pch = 19, col = "steelblue")
abline(h = 0, lty = 2, col = "gray")
qqnorm(residuals, main = "Normal Q-Q Plot", pch = 19, col = "steelblue")
qqline(residuals, col = "red")
plot(fitted_vals, sqrt(abs(rstandard(model))), main = "Scale-Location", xlab = "Fitted values", ylab = "√|Standardized residuals|", pch = 19, col = "darkorange")
hist(residuals, main = "Residual Distribution", xlab = "Residual", col = "seagreen", border = "white")
dev.off()

cat("=== Linear Regression Diagnostics (R) ===\n")
cat("Observations:", nrow(data), "\n")
cat("Intercept:", round(intercept, 2), "\n")
cat("Slope (", x_col, "):", round(slope, 2), "\n", sep = "")
cat("R-squared:", round(r_squared, 4), "\n")
cat("Adjusted R-squared:", round(adj_r_squared, 4), "\n")
cat("RMSE:", round(rmse, 2), "\n")
cat("Residual mean:", round(mean(residuals), 2), "\n")
cat("Residual std:", round(sd(residuals), 2), "\n")
cat("Max |residual|:", round(max(abs(residuals)), 2), "\n")
cat("Max Cook's distance:", round(max(cooks.distance(model)), 4), "\n")
print(summary(model))
cat("Saved plot to linear_regression_r_output.png\n")
cat("Saved annotated plot to regression_plot_r.png\n")
cat("Saved diagnostics to regression_diagnostics_r.png\n")
