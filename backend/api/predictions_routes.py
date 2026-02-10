from fastapi import APIRouter
import pandas as pd 
from ml_engine.predictor import get_recommendations
from pathlib import Path


router = APIRouter()
BASE_DIR = Path(__file__).resolve().parents[1] 
DATA_PATH = BASE_DIR / "data" / "processed" / "features.parquet"

@router.get("/recommend")
def recommend():
    df = pd.read_parquet(DATA_PATH)
    df = get_recommendations(df)

    top = (
        df.sort_values("upside", ascending=False)
          .head(10)
    )

    return [
        {
            "player_id": int(row["personId"]),
            "name": row["playerName"],
            "team": row["teamName"],
            "predicted_fp": round(row["predicted_fp"], 1),
            "upside": round(row["upside"], 1),
            "explanations": {
                "usage_proxy": round(row["contrib_usage_proxy"], 2),
                "recent_form": round(row["contrib_rolling_FPoint_Last5"], 2),
                "minutes_trend": round(row["contrib_rolling_Min_Last10"], 2),
                "volatility": round(row["contrib_rolling_FPointsVol_Last5"], 2),
            }
        }
        for _, row in top.iterrows()
    ]
