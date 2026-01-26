import pandas as pd
import numpy as np

def compute_recommendation_score(row):
    """
    Computes a fantasy pickup score for a player.
    Higher = Better .
    """

    # Recent improvement in fantasy output
    upside = row["rolling_FPoint_Last5"] - row["rolling_FPoint_Last10"]

    # Change in playing time
    minutes_trend = row["rolling_Min_Last5"] - row["rolling_Min_Last10"]

    # Baseline recent performance
    recent_fp = row["rolling_FPoint_Last5"]

    score = (
        0.3 * upside +
        0.5 * minutes_trend +
        0.2 * recent_fp
    )

    return score, upside, minutes_trend, recent_fp

def get_recommendations(df, top_n = 10):
    """
    Returns the top 10 fantasy pickup recommendation
    """
    df = df.copy()
    
    # Replace invalid values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    # Use latest game per player
    latest = (
        df.sort_values("gameDateTimeEst")
          .groupby("personId")
          .tail(1)
          .copy()
    )

    results = []

    for _, row in latest.iterrows():
        score, upside, minutes_trend, recent_fp = compute_recommendation_score(row)

        results.append({
            "player_id": int(row["personId"]),
            "name": row["player_name"],
            "team": row["teamName"],
            "score": round(score, 2),
            "recent_fp": round(recent_fp, 1),
            "upside": round(upside, 1),
            "minutes_trend": round(minutes_trend, 1),
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)[:top_n]
