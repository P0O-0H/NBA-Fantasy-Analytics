import pandas as pd
from pathlib import Path

RAW_PATH = Path("backend/data/raw_game_logs/clean_data.csv")
DEST_PATH = Path("backend/data/processed/game_logs.parquet")

def main():
    df = pd.read_csv(RAW_PATH)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns = "Unnamed: 0")
    
    df["player_name"] = df["firstName"].astype(str) + " " + df["lastName"].astype(str)

    if "numMinutes" in df.columns:
        df.rename(columns = {"numMinutes": "minutes"})
    
    df["gameDateTimeEst"] = pd.to_datetime(df["gameDateTimeEst"], errors="coerce")

    stat_cols = [
        "minutes",
        "fantasyPoints",
        "points",
        "assists",
        "rebounds",
        "steals",
        "blocks",
        "turnovers"
    ]

    for col in stat_cols:
        if col in df.columns:
            pd.to_numeric(df[col], errors = "coerce").fillna(0)

    df = df.dropna(subset= ["personId", "gameDateTimeEst"])
    df = df.drop_duplicates(subset= ["personId", "gameDateTimeEst"])
    df = df.sort_values(["personId", "gameDateTimeEst"])

    DEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(DEST_PATH, index=False)

    print(f"Saved canonical game logs to {DEST_PATH}")
    print(f"Rows: {len(df):,}")
    print(f"Players: {df['personId'].nunique():,}")

if __name__ == "__main__":
    main()