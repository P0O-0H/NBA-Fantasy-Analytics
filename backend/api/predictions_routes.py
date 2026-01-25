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
    return get_recommendations(df)
