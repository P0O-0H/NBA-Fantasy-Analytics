import pandas as pd
import numpy as np
import joblib



MODEL_PATH = "ml_engine/models/ridge_model.joblib"
DATA_PATH = "data/processed/ml_dataset.parquet"

FEATURE_COLS = [
    "rolling_FPoint_Last5",
    "rolling_FPoint_Last10",
    "rolling_Min_Last5",
    "rolling_Min_Last10",
    "rolling_FPointsVol_Last3",
    "rolling_FPointsVol_Last5",
    "usage_proxy",
]

model = joblib.load(MODEL_PATH)


def explain_prediction(row):
    """
    Break prediction into feature contributions.
    """
    coefs = model.named_steps["model"].coef_
    values = row[FEATURE_COLS].values

    return {
        feature: float(coef * val)
        for feature, coef, val in zip(FEATURE_COLS, coefs, values)
    }

def generate_prediction(top_n = 20):
    """
    Main inference function for prediction
    """
    df = pd.read_parquet(DATA_PATH)

    df = df.dropna()
    
    X = df[FEATURE_COLS]
    preds = model.predict(X)

    df = df.copy()
    df["predicted_fp"] = preds
    df["baseline_fp"] = df["rolling_FPoint_Last10"]
    df["upside"] = df["predicted_fp"] - df["baseline_fp"]

    results = []

    for _, row in (
        df.sort_values("upside", ascending=False)
        .head(top_n)
        .iterrows()
    ):
        results.append({
            "player_id": int(row["personId"]),
            "name": row["player_name"],
            "team": row["teamName"],
            "predicted_fp": float(row["predicted_fp"]),
            "baseline_fp": float(row["baseline_fp"]),
            "upside": float(row["upside"]),
            "minutes_trend": float(row["rolling_Min_Last5"]),
            "drivers": explain_prediction(row),
        })

    return results
