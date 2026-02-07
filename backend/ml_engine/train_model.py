import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

DATA_PATH = "data/processed/features.parquet"
TARGET = "fantasyPoints"
RANDOM_STATE = 67

FEATURES = [
    "rolling_FPoint_Last5",
    "rolling_FPoint_Last10",
    "rolling_Min_Last5",
    "rolling_Min_Last10",
    "rolling_FPointsVol_Last3",
    "rolling_FPointsVol_Last5",
    "usage_proxy"
]

df = pd.read_parquet(DATA_PATH)

df = df[df["minutes"] > 0]

df = df.dropna(subset=FEATURES + [TARGET])

print(f"Dataset size after cleaning: {len(df):,}")

# IMPORTANT: split by time, not random
df = df.sort_values("gameDateTimeEst")

train_size = int(len(df) * 0.8)
train_df = df.iloc[:train_size]
test_df = df.iloc[train_size:]

X_train = train_df[FEATURES]
y_train = train_df[TARGET]

X_test = test_df[FEATURES]
y_test = test_df[TARGET]

pipeline = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]
)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
#rmse = mean_absolute_error(y_test, y_pred, squared=False)

print("\nModel Performance")
print(f"MAE  : {mae:.2f}")
#print(f"RMSE : {rmse:.2f}")

coef_df = pd.DataFrame({
    "feature": FEATURES,
    "coefficient": pipeline.named_steps["model"].coef_
}).sort_values("coefficient", ascending=False)

print("\nFeature importance (Ridge coefficients)")
print(coef_df)
