import pandas as pd

df = pd.read_parquet("data/processed/features.parquet")

df.sort_values(["player_id", "gameDateTimeEst"])

df["target_fp_next"] = (
    df.groupby("player_id")["fantasyPoints"].shift(-1)
)

ml_df = df.dropna(subset=["target_fp_next"])

features = [
    "rolling_FPoint_Last10",
    "rolling_Min_Last10",
    "usage_proxy",
    "rolling_FPointsVol_Last5"
]

ml_df = ml_df[
    ["player_id", "gameDateTimeEst", "target_fp_next"] + features
]

# Save ML dataset
ml_df.to_parquet(
    "data/processed/ml_dataset.parquet",
    index=False
)

print("ML dataset built:", ml_df.shape)