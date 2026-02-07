import pandas as pd
from sklearn.metrics import mean_absolute_error

df = pd.read_parquet("data/processed/ml_dataset.parquet")

y_real = df["target_fp_next"]
y_pred = df["rolling_FPoint_Last10"]

mask = y_pred.notna()
y_real = y_real[mask]
y_pred = y_pred[mask]

mean_abs_err = mean_absolute_error(y_real, y_pred)
print(f"Baseline MAE (rolling last 10): {mean_abs_err:.5f}")
print(f"Evaluated on {len(y_real)} samples")