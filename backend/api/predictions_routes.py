from fastapi import APIRouter

router = APIRouter()

@router.get("/recommend")
def recommend():
    return [
        {
            "player_id": "123",
            "name": "Dummy Player",
            "avg_fp": 32.5,
            "predicted_fp": 40.1,
            "upside": 7.6,
            "confidence": 0.75
        },
        {
            "player_id": "456",
            "name": "Another Player",
            "avg_fp": 28.9,
            "predicted_fp": 35.4,
            "upside": 6.5,
            "confidence": 0.68
        }
    ]