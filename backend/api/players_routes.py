from pathlib import Path
import pandas as pd
from fastapi import APIRouter

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[1]  # backend/
DATA_PATH = BASE_DIR / "data" / "processed" / "features.parquet"

DF = pd.read_parquet(DATA_PATH)

@router.get("/{player_id}/timeseries")
def player_timeseries(player_id: int):
    df = DF[DF["personId"] == player_id].sort_values("gameDateTimeEst")

    if df.empty:
        return {"player_id": player_id, "data": []}

    def safe(series):
        return [
            float(x) if pd.notna(x) else 0.0
            for x in series.tolist()
        ]

    return {
        "player_id": int(player_id),
        "dates": [d.strftime("%Y-%m-%d") for d in df["gameDateTimeEst"]],
        "fantasy_points": safe(df["fantasyPoints"]),
        "rolling_FPoint_Last5": safe(df["rolling_FPoint_Last5"]),
        "rolling_FPoint_Last10": safe(df["rolling_FPoint_Last10"]),
        "minutes": safe(df["minutes"]),
        "rolling_Min_Last5": safe(df["rolling_Min_Last5"]),
    }