import pandas as pd
from pathlib import Path

IN_PATH = Path("backend/data/processed/game_logs.parquet")
DEST_PATH = Path("backend/data/processed/features.parquet")

def main():
    df = pd.read_parquet(IN_PATH)

    df = df.sort_values(["personId", "gameDateTimeEst"])

    df["rolling_FPoint_Last5"] = df.groupby("personId")["fantasyPoints"].rolling(window= 5).mean().reset_index(drop = True)
    df["rolling_FPoint_Last10"] = df.groupby("personId")["fantasyPoints"].rolling(window= 10).mean().reset_index(drop = True)
    df["rolling_Min_Last5"] = df.groupby("personId")["minutes"].rolling(window= 5).mean().reset_index(drop = True)
    df["rolling_FPointsVol_Last3"] = df.groupby("personId")["minutes"].rolling(window= 3).std().reset_index(drop = True).fillna(0)
    df["rolling_FPointsVol_Last5"] = df.groupby("personId")["minutes"].rolling(window= 5).std().reset_index(drop = True).fillna(0)

    if all(c in df.columns for c in ["fieldGoalsAttempted", "freeThrowsAttempted", "assists"]):
        df["usage_proxy"] = (
            df["fieldGoalsAttempted"]
            + 0.44 * df["freeThrowsAttempted"]
            + df["assists"]
        )
    else:
        df["usage_proxy"] = 0
    
    DEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(DEST_PATH, index=False)

    print(f"Saved feature dataset: {DEST_PATH}")
    print(f"Rows: {len(df):,}")

if __name__ == "__main__":
    main()
    


